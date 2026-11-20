# Copyright 2025 ForgeFlow S.L. (https://www.forgeflow.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    rewards = env["loyalty.reward"].search([("description", "=", False)])
    rewards._compute_description()
    # Odoo retries the NOT NULL on description in finalize_constraints, after
    # the end-migration scripts, and the retry reads the values from SQL: flush
    # them now to let the constraint be set in this same run.
    env.flush_all()
