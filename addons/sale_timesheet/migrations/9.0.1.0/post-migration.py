# -*- coding: utf-8 -*-
# © 2016 Opener B.V. - Stefan Rijnhart
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade


def set_hr_employee_timesheet_cost(cr):
    """ Obsolete field 'product_id' from hr_timesheet in 8.0 is replaced
    by a field timesheet_cost in this module.
    """

    openupgrade.logged_query(
        cr, """\
            UPDATE hr_employee he
            SET timesheet_cost = ip.value_float
            FROM ir_property ip
            WHERE ip.res_id = CONCAT('product.product,', he.product_id)
            AND ip.name = 'standard_price'
            """)


@openupgrade.migrate(no_version=True)
def migrate(cr, version):
    if openupgrade.is_module_installed(cr, 'hr_timesheet'):
        set_hr_employee_timesheet_cost(cr)
