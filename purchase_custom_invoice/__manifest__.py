# -*- coding: utf-8 -*-

{
    'name': 'custom purchase invoice report',
    'version': '1.0',
    'license': 'LGPL-3',
    'author': 'ziad',
    'category': 'Purchase/Sales',
    'summary': 'custom purchase invoice',
    'description': """
        This module provide inherit pdf report includes managing
            * Admission
    """,
    'depends': [
        'purchase' ,'sale'
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'report/purchase_custom_report.xml',
        'report/purchase_order_custom_template.xml',
    
    ],
 
}
