# Copyright 2026 Binhex <https://www.binhex.cloud>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    """Turn the dead v14-17 'product' type default into consu + storable."""
    defaults = env["ir.default"]
    storable = env["ir.model.fields"]._get("product.template", "is_storable")
    env.cr.execute(
        """
        SELECT user_id, company_id, condition
        FROM ir_default
        WHERE field_id = %s AND json_value = '"product"'
        """,
        (env.ref("product.field_product_template__type").id,),
    )
    for user_id, company_id, condition in env.cr.fetchall():
        scope = dict(user_id=user_id, company_id=company_id, condition=condition)
        # ir.default.set() invalidates the defaults cache, raw SQL would not
        defaults.set("product.template", "type", "consu", **scope)
        if storable:
            defaults.set("product.template", "is_storable", True, **scope)
