# -*- coding: utf-8 -*-
# License, author and contributors information in:
# __openerp__.py file at the root folder of this module.
from openerp import models, fields


class ProductProduct(models.Model):
    _inherit = 'product.template'

    product_qty_package = fields.Float(
        string='UoPackage',
        readonly=True,
        default=1)
