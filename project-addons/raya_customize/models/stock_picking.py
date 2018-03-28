# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
from openerp import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    partner_category_id = fields.Many2many(
        related='partner_id.category_id',
        store=True)
