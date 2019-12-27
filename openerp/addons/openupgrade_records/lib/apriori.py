""" Encode any known changes to the database here
to help the matching process
"""

renamed_modules = {
    'base_calendar': 'calendar',
    'mrp_jit': 'procurement_jit',
    'project_mrp': 'sale_service',
    # OCA/account-invoice-reporting
    'base_condition_template': 'base_comment_template',
    # OCA/account-invoicing
    'invoice_validation_wkfl': 'account_invoice_validation_workflow',
    'account_invoice_zero': 'account_invoice_zero_autopay',
    # OCA/account-payment
    'paydays': 'account_payment_term_multi_day',
    # OCA/sale-reporting
    'sale_condition_template': 'sale_comment_template',
    # OCA/server-tools
    'audittrail': 'auditlog',
    # OCA/bank-statement-import
    'account_banking': 'account_bank_statement_import',
    'account_banking_camt': 'account_bank_statement_import_camt',
    'account_banking_mt940':
        'account_bank_statement_import_mt940_base',
    'account_banking_nl_ing_mt940':
        'account_bank_statement_import_mt940_nl_ing',
    'account_banking_nl_rabo_mt940':
        'account_bank_statement_import_mt940_nl_rabo',
    # OCA/product-attribute
    'product_images': 'product_multi_image',
    # OCA/hr-timesheet
    'hr_timesheet_holidays': 'hr_timesheet_holiday',
    # OCA/web
    'web_popup_large': 'web_dialog_size',
    # other
    'account_central_journal': 'l10n_it_central_journal',
    'invoice_mail_send': 'account_invoice_always_email',
    'web_polymorphic': 'web_polymorphic_field',
    'mail_organizer': 'email_organizer',
    'omnia_ddt': 'l10n_it_ddt',
    'enlarge_form_sheet': 'web_sheet_full_width',
    'stock_invoice_picking_incoterm': 'stock_picking_invoicing_incoterm',
    'techplus_l10n_it_invoice_intra_cee': 'l10n_it_invoice_intra_cee', #?
    'techplus_l10n_it_corrispettivi': 'l10n_it_corrispettivi',
    'techplus_l10n_it_vat_registries': 'l10n_it_vat_registries',
    'techplus_l10n_it_withholding_tax': 'l10n_it_withholding_tax',
    'techplus_l10n_it_ricevute_bancarie': 'l10n_it_ricevute_bancarie',
    'techplus_l10n_it_partially_deductible_vat': 'l10n_it_partially_deductible_vat',
    'techplus_account_vat_period_end_statement': 'account_vat_period_end_statement',
    'techplus_account_fiscal_year_closing': 'account_fiscal_year_closing',
    'techplus_account_due_list': 'account_due_list',
    'techplus_account_voucher_cash_basis': 'account_voucher_cash_basis',
    'techplus_account_financial_report': 'account_financial_report',
}
merged_modules = {
    'report_aeroo_ooo': 'report_aeroo',
}
renamed_models = {
}
