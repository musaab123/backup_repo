# -*- coding: utf-8 -*-

{
    'name': 'custom Hr Expense,Stock Report',
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
        'hr_expense','hr'
    ],
    'data': [
         'report/sale_report_inherit.xml',
        'report/page_content_custom.xml',
 
    
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
