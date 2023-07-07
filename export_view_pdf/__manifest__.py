# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2022-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
{
    'name': "Export View PDF",
    'description': """Export View PDFf""",
    'summary': """Export Current List View in PDF Format""",
    'version': '16.0.1.0.0',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'depends': ['base', 'account','sale','purchase'],
    'data':
        [
            'views/pdf.xml',
            'views/pdf_group_by_template.xml',
        ],
    'assets': {
        'web.assets_backend': [
            'export_view_pdf/static/src/views/pdf_export.js',
            'export_view_pdf/static/src/views/list_button_view.xml'
        ]
    },
    'images': [
        'static/description/banner.png'
    ],

    'pre_init_hook' :'pre_install',
    'pre_init_hook' :'pre_install_l',
    'pre_init_hook' :'pre_install_o',
    'pre_init_hook' :'pre_install_u',
    'pre_init_hook' :'pre_install_s',
    'pre_init_hook' :'pre_install_p',
    'pre_init_hook' :'pre_install_pur_1',
    'pre_init_hook' :'pre_install_pur_2',





    'pre_init_hook' :'pre_install_c',
    'pre_init_hook' :'pre_install_v',
    'pre_init_hook' :'pre_install_x',

    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
