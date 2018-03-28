# -*- coding: utf-8 -*-
# License, author and contributors information in:
# __openerp__.py file at the root folder of this module.
from openerp import models, fields


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_qty_package = fields.Float(
        related='product_id.product_qty_package',
        readonly=True)
