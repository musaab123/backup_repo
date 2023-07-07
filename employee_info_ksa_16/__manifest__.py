# -*- coding: utf-8 -*-


{
    'name': 'Employee Informations (Saudi Arabia Version)',
    'version': '16.0.1.0.0',
    'category': 'Human Resources',
    'description': 'Adding saudi market required extra Fields In employee profile.',
    'summary': 'Adding saudi market required extra Fields In employee profile',
    'author': 'iUXING Technologies',
    'company': 'iUXING',
    'website': 'https://iuxing.com',
    'maintainer': 'Rami A. Nasrallah',
    'depends': ['base', 'hr', 'mail', 'hr_gamification','hr_contract'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/contract_days_view.xml',
        'views/updation_config.xml',
        'views/hr_employee_view.xml',
        'views/hr_notification.xml',
    ],
    'images': ['static/description/banner.png'],
    'price': '0',
    'currenct': 'EUR',
    'support': 'info@iuxing.com',
    'installable': True,
    'application': False,
    'license': 'AGPL-3',
}

