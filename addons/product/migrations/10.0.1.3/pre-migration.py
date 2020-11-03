# -*- coding: utf-8 -*-
# © 2017 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade

_column_copies = {
    'res_partner': [
        ('property_product_pricelist', 'property_product_pricelist_m2o', None),
    ],
}


@openupgrade.migrate(use_env=False)
def migrate(cr, version):
    if openupgrade.column_exists(cr, 'res_partner', 'property_product_pricelist'):
        openupgrade.copy_columns(cr, _column_copies)
