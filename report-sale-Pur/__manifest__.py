# -*- coding: utf-8 -*-

{
    'name': 'inherit pdf report',
    'version': '1.0',
    'license': 'LGPL-3',
    'author': 'team-2 course',
    'category': 'Purchase/Sales',
    'summary': 'inherit pdf report',
    'description': """
        This module provide inherit pdf report includes managing
            * Admission
    """,
    'depends': [
        'sale' 
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'report/sale_report_inherit.xml',
        'report/sale_custom_report_inh.xml',
        


        
   


    
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
