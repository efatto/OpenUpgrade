# Copyright 2020 Sergio Corato <https://github.com/sergiocorato>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade
from psycopg2 import sql


def create_property_product_pricelist_from_m2o(env):
    # per ogni partner con il campo property_product_pricelist,
    # creare property_product_pricelist in ir.property se non esiste
    env.cr.execute(
        sql.SQL(
            "SELECT id FROM res_partner "
            "WHERE property_product_pricelist_m2o IS NOT NULL"
        )
    )
    partners = env['res.partner'].browse(x[0] for x in env.cr.fetchall())
    env.cr.execute("SELECT id FROM ir_model_fields WHERE model=%s AND name=%s",
                   ('res.partner', 'property_product_pricelist'))
    fields_id = env.cr.fetchone()
    for partner in partners:
        openupgrade.logged_query(
            env.cr, sql.SQL(
                """
                INSERT INTO ir_property
                (name, res_id, company_id, fields_id, value_reference, type)
                SELECT
                    'property_product_pricelist',
                    CONCAT('res.partner,', %s),
                    %s,
                    %s,
                    CONCAT('product.pricelist,', p.property_product_pricelist_m2o),
                    'many2one'
                FROM
                    res_partner as p
                WHERE p.id = %s
                AND NOT EXISTS(SELECT 1
                                  FROM ir_property
                                 WHERE fields_id=%s
                                   AND company_id=%s
                                   AND res_id=CONCAT('res.partner,', %s))
                """
            ), (partner.id, partner.company_id.id, fields_id,
                partner.id,
                fields_id, partner.company_id.id, partner.id)
        )


@openupgrade.migrate()
def migrate(env, version):
    if openupgrade.column_exists(
            env.cr, 'res_partner', 'property_product_pricelist_m2o'):
        create_property_product_pricelist_from_m2o(env)
