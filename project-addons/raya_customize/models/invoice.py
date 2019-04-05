# -*- coding: utf-8 -*-
# License, author and contributors information in:
# __openerp__.py file at the root folder of this module.

from openerp import models, fields


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    payment_responsible_id = fields.\
        Many2one("res.users", "Collector", readonly=True,
                 related="partner_id.payment_responsible_id", store=True)
