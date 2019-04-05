# -*- coding: utf-8 -*-
###############################################################################
#
#    Trey, Kilobytes de Soluciones
#    Copyright (C) 2017-Today Trey, Kilobytes de Soluciones <www.trey.es>
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
###############################################################################
{
    'name': 'Personalización Grupo Raya',
    'summary': 'Personalización para la instancia de Odoo de Grupo Raya.',
    'category': 'Custom',
    'version': '8.0.0.1',
    'description': '''Personalización para la instancia de
     Odoo de Grupo Raya.''',
    'author': 'Trey Kilobytes de Soluciones (www.trey.es)',
    'website': 'http://www.trey.es',
    'depends': [
        'base',
        'web',
        'sale',
        'stock',
        'account',
        'l10n_es',
        'account_followup',
        'l10n_es_partner',
        'l10n_es_toponyms',
        'report',
        'mass_editing',
        'account_banking_sepa_credit_transfer',
        'account_banking_sepa_direct_debit',
        'account_payment_partner',
        'account_payment_purchase',
        'account_payment_sale',
        'account_payment_sale_extender',
        'account_payment_sale_stock',
        'account_followup',
        'account_invoice_merge_stock_move',
        'print_formats_base',
        'print_formats_account',
        'print_formats_sale',
        'print_formats_stock',
        'product_label_picking',
        'sale_filter_addresses_with_customer',
        'purchase_discount',
        'purchase_landed_cost',
        'purchase_landed_cost_extender',
        'sale_commission',
        'sale_stock',
        'note',
        'product_visible_discount',
        'product_supplierinfo_discount',
        'purchase_pricelist_partnerinfo',
        'product_pricelist_partnerinfo',
        'purchase_discount_quand_cost',
        'purchase_report_discount_cost',
        'account_invoice_merge',
        'account_invoice_merge_payment',
        'account_invoice_merge_purchase',
        'stock_picking_invoice_link',
    ],
    'data': [
        'data/report_paperformat.xml',
        'views/webclient_templates.xml',
        'views/product_view.xml',
        'views/sale_view.xml',
        'views/pricelist_partnerinfo_view.xml',
        'views/stock_view.xml',
        'views/account_invoice_view.xml',
        'report/report_layout.xml',
        'report/report_invoice.xml',
        'report/report_saleorder.xml',
        'report/report_stockpicking.xml',
        'report/report_product_label_picking.xml',
        'report/report_product_label.xml',
    ],
    'installable': True,
}
