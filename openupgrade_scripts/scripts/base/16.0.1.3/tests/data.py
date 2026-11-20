from odoo import fields

env = locals().get("env")
# set company_registry in v15 to be sure we migrate it correctly to v16
env.ref("base.main_company").company_registry = "424242"
# create the same bank account for the same partner in two companies: the new
# unique(sanitized_acc_number, partner_id) constraint does not allow it, so the
# pre-migration must keep only one record
company = env["res.company"].create({"name": "OpenUpgrade Test Company"})
partner = env["res.partner"].create(
    {"name": "OpenUpgrade Test Partner", "is_company": True}
)
bank = env["res.bank"].create({"name": "OpenUpgrade Test Bank"})
env["res.partner.bank"].create(
    [
        {
            "acc_number": "OPENUPGRADE TEST ACCOUNT",
            "partner_id": partner.id,
            "bank_id": bank.id,
            "company_id": env.ref("base.main_company").id,
        },
        {
            "acc_number": "OPENUPGRADE TEST ACCOUNT",
            "partner_id": partner.id,
            "bank_id": bank.id,
            "company_id": company.id,
        },
    ]
)

# translated name of a user-created scheduled action: ir.actions.* names are
# excluded from the generic pre-migration translation update, the base
# post-migration must merge their translations
action = env["ir.actions.server"].create(
    {
        "name": "OpenUpgrade Test Action",
        "model_id": env.ref("base.model_res_partner").id,
        "state": "code",
        "code": "pass",
    }
)
env["ir.cron"].create(
    {
        "ir_actions_server_id": action.id,
        "cron_name": "OpenUpgrade Test Action",
        "user_id": env.uid,
        "interval_number": 1,
        "interval_type": "months",
        "nextcall": fields.Datetime.now(),
    }
)
action.with_context(lang="fr_FR").write({"name": "Action de test OpenUpgrade"})
env.cr.commit()
