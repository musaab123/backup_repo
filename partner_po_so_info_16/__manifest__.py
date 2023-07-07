# -*- coding: utf-8 -*-


{
    'name': 'Informations of Partners,SO and PO',
    'version': '16.0.1.0.0',
    'category': 'Contacts',
    'description': 'Adding new information fields in partners,sales,purchase and accounts.',
    'summary': 'Adding new information fields in partners,sales,purchase and accounts.',
    'author': 'PROSYS',
    'company': 'PROSYS',
    'maintainer': 'ZIAD HASSAN',
    'depends': ['base', 'sale', 'purchase', 'account' ,'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/sales_view.xml',
        'views/purchase_view.xml',
        'views/accounts_view.xml',
        'views/partner_view.xml',
        'views/stock_view.xml',

    ],
    'installable': True,
    'application': False,
}

