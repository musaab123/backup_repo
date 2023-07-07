# -*- coding: utf-8 -*-
{
    'name':'Presys Clothes Custom',
    'version':'1.0',
    'category':'Presys Clothes Custom',
    'sequence':14,
    'summary':'',
    'description':""" clothes shop Management""",
    'author':'Presys',
    'depends':['base','sale','purchase'],
    'data':[
        'views/sale_custom_inherit.xml',
        'views/sale_order_imherit.xml',
        'views/purchase_order_inherit.xml',
        'report/purchase_custom_report.xml',


        



    ],
    'images': ['static/description/images/splash-screen.jpg'],
    'installable':True,
    'auto_install':False,
    'currency': 'EUR',
    'price': 600,
    'application':True,
    'license': "AGPL-3",
}