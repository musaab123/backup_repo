# -*- coding: utf-8 -*-

{
    'name': "Expenses Portal",
    'version': '16.0.1.2',
    'summary': """
        Apply Expenses from portal.Easily access to expenses and apply expenses from portal.User can easily  from portal.""",
    'description': """
        =>Apply Expenses from portal.Easily access to expense and apply expense from portal.
        =>User can easily create expense from portals.
        =>Showninf old expenses lines data.
    """,
    'category': 'Human Resources/Attendance',
    'author': 'Prosys',
    'company': 'PROSYS',
    'depends': ['hr', 'portal', 'portal_hr_knk','sh_hr_attendance_geolocation','employee_extra_data'],
    'data': [
        'views/portal_expense_templates.xml',
        
    ],
    # 'assets': {
    #     'web.assets_backend': [
    #         '/hr_expense/static/src/**/*',
    #         '/hr_expense/static/src/xml/**/*',
    #     ],
    #     'web.assets_frontend': [
    #         '/portal_expenses/static/src/js/attendance_portal.js',
    #         '/portal_expenses/static/src/js/checkin_out.js',
    #     ],
    # },
    'installable': True,
    'application': False,
    'auto_install': False,
}
