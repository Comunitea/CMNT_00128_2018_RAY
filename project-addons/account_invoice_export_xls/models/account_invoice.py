# -*- coding: utf-8 -*-
# License, author and contributors information in:
# __openerp__.py file at the root folder of this module.
from openerp.osv import orm


class AccountInvoice(orm.Model):
    _inherit = 'account.invoice'

    def _report_xls_fields(self, cr, uid, context=None):
        return [
            'date_invoice', 'invoice_number', 'partner_name', 'partner_vat',
            'amount_untaxed', 'amount_taxed', 'amount_total',
            'tax_line_description', 'tax_line_base', 'tax_line_amount'
        ]



    def _report_xls_template(self, cr, uid, context=None):
        return {}
