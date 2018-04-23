# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
from openerp import fields, models
import openerp.addons.decimal_precision as dp


class StockPicking(models.Model):
    _inherit = "stock.picking"

    partner_category_id = fields.Many2many(
        related='partner_id.category_id',
        store=True)


class StockMove(models.Model):

    _inherit = "stock.move"

    qty_available = fields.\
        Float('Qty available', readonly=True,
              related='product_id.qty_available',
              digits_compute=dp.get_precision('Product Unit of Measure'))
