# -*- coding: utf-8 -*-
###################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2022-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###################################################################################
{
    'name': 'Product Brand in Inventory',
    'version': '16.0.1.0.0',
    'category': 'Warehouse',
    'summary': 'Product Brand in Inventory',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'images': ['static/description/banner.png'],
    'website': 'https://www.cybrosys.com',
    'depends': ['stock','sale_management','purchase','account'],
    'data': [
        'security/ir.model.access.csv',
        'views/brand_views.xml',
        'views/brand_sale_views.xml',
        'views/sale_report_views.xml',
        'views/brand_purchase_views.xml',
        'views/purchase_report_views.xml',
        'views/account_invoice_report_view.xml',
        'views/brand_invoice_views.xml'
        
    ],
    
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,

}
