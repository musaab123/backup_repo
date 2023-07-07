# -*- coding: utf-8 -*-

{
    'name': 'custom Stock Report',
    'version': '1.0',
    'license': 'LGPL-3',
    'author': 'team-2 course',
    'category': 'Purchase/Sales/Stock/Hr_expense',
    'summary': 'custom Hr Expense,Stock Report',
    'description': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com
    """,
    'depends': [
        'stock'
    ],
    'data': [
        # 'security/ir.model.access.csv',
      
        #   'report/delivery_note_custom.xml',
        #   'report/delivery_page_custom.xml',
          'report/stock_slip_custom.xml',
          'report/stock_page_slip_custom.xml',
    
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
