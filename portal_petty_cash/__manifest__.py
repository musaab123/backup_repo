# -*- coding: utf-8 -*-

{
    'name': "Petty Cash Portal",
    'version': '16.0.1.2',
    'summary': """
        Apply Petty Cash from portal.Easily access to Petty Cash and apply Petty Cash from portal.User can easily  from portal.""",
    'description': """
        =>Apply Petty Cash from portal.Easily access to expense and apply expense from portal.
        =>User can easily create expense from portals.
        =>Showninf old Petty Cash lines data.
    """,
    'category': 'Human Resources/Petty Cash',
    'author': 'Prosys',
    'company': 'PROSYS',
    'depends': ['hr_expense', 'portal', 'portal_hr_knk','sh_hr_attendance_geolocation','petty_cash_management','petty_cash_extention'],
    'data': [
        'views/portal_petty_cash_templates.xml',
        
    ],
    'assets': {
        'web.assets_backend': [
            '/petty_cash_management/static/src/**/*',
            '/petty_cash_management/static/src/xml/**/*',
        ],
        'web.assets_frontend': [
            '/portal_petty_cash/static/src/js/attendance_portal.js',
            '/portal_petty_cash/static/src/js/checkin_out.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
