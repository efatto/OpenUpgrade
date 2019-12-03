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
    'account_financial_report': 'account_financial_report_webkit',
    'omnia_ddt': 'l10n_it_ddt',
    'account_invoice_merge_no_unlink': 'account_invoice_merge',
    'enlarge_form_sheet': 'web_sheet_full_width',
    'stock_invoice_picking_incoterm': 'stock_picking_invoicing_incoterm',
}

renamed_models = {
}
