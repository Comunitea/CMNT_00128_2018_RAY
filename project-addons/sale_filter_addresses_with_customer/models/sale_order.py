# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2014 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    partner_invoice_id = fields.Many2one(
        comodel_name='res.partner',
        string='Invoice Address',
        readonly=True,
        required=True,
        domain=("['|', ('id', '=', partner_id), '&', "
                "('id', 'child_of', partner_id), ('type', '=', 'invoice')]"),
        states={'draft': [('readonly', False)],
                'sent': [('readonly', False)]},
        help="Invoice address for current sales order.")

    partner_shipping_id = fields.Many2one(
        comodel_name='res.partner',
        string='Delivery Address',
        readonly=True,
        required=True,
        domain=("['|', ('id', '=', partner_id), '&', "
                "('id', 'child_of', partner_id), ('type', '=', 'delivery')]"),
        states={'draft': [('readonly', False)],
                'sent': [('readonly', False)]},
        help="Delivery address for current sales order.")
