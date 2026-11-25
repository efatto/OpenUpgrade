from odoo.tests import TransactionCase, tagged

from odoo.addons.openupgrade_framework import openupgrade_test


@openupgrade_test
class TestProductMigration(TransactionCase):
    def test_pricelist(self):
        partner = self.env.ref("base.user_demo").partner_id
        company = self.env["res.company"].search(
            [
                ("name", "=", "Product migration test company"),
            ]
        )
        pricelist_main = self.env["product.pricelist"].search(
            [
                ("name", "=", "Pricelist for main company"),
            ]
        )
        pricelist = self.env["product.pricelist"].search(
            [
                ("name", "=", "Pricelist for demo company"),
            ]
        )
        self.assertTrue(company)
        self.assertTrue(pricelist)
        self.assertEqual(partner.property_product_pricelist, pricelist_main)
        self.assertEqual(
            partner.with_company(company).property_product_pricelist, pricelist
        )


@openupgrade_test
@tagged("post_install", "-at_install")
class TestProductTypeDefault(TransactionCase):
    def test_product_type_defaults(self):
        product = self.env["product.template"].create({"name": "Default type"})
        self.assertEqual(product.type, "consu")
        if "is_storable" in product._fields:
            self.assertTrue(product.is_storable)
