# -*- coding: utf-8 -*-
# License, author and contributors information in:
# __openerp__.py file at the root folder of this module.
from openerp import models, fields


class PosCategory(models.Model):
    _inherit = 'pos.category'

    internal_categ_id = fields.Integer(
        string='Internal category Id',
        readonly=True,
        help="This field only is used for 'pos_categories' odoocli script.")
