# -*- coding: utf-8 -*-
{
    'name': "cybat_pos_discount",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Cybat",
    'website': "https://www.cybat.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['pos_discount','pos_hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'assets': {
        'point_of_sale.assets': [
            'cybat_pos_discount/static/src/js/**/*',
        ],
         'point_of_sale.assets': [
            'cybat_pos_discount/static/src/xml/**/*',
        ],
    },
}
