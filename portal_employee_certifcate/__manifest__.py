# -*- coding: utf-8 -*-
# Powered by Kanak Infosystems LLP.
# © 2020 Kanak Infosystems LLP. (<https://www.kanakinfosystems.com>).

{
    'name': 'Certifacte Portal Employee',
    'version': '16.0.1.0',
    'category': 'Human Resources/Payroll',
    'summary': 'Certifacte Portal',
    'description': 'Employee can see their Certifacate and also download it. Seacrh the Certifacate by Date. Chat with head using chatter',
    'author': 'Prosys.',
    'website': 'https://www.kanakinfosystems.com',
    'license': 'OPL-1',
    'depends': ['hr' ,'portal','portal_hr_knk'],
    'data': [
        'views/portal_template.xml',
    ],

    
    'images': ['static/description/banner.gif'],
    'application': True,
    'installable': True,
    'price': 60,
    'currency': 'EUR'
}
