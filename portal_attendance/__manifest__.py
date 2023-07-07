# -*- coding: utf-8 -*-

{
    'name': "Attendance Portal",
    'version': '16.0.1.2',
    'summary': """
        Apply attendance from portal.Easily access to leave and apply leave from portal.User can easily check in/out from portal.""",
    'description': """
        =>Apply attendance from portal.Easily access to leave and apply leave from portal.
        =>User can easily check in/out from portals.
        =>Showninf old attendance lines data.
    """,
    'category': 'Human Resources/Attendance',
    'author': 'ZIAD MONIM',
    'company': 'PROSYS',
    'depends': ['hr_attendance', 'portal', 'portal_hr_knk','sh_hr_attendance_geolocation'],
    'data': [
        'views/check_in_out_view.xml',
        'views/portal_templates.xml',
        
    ],
    'assets': {
        'web.assets_backend': [
            '/hr_attendance/static/src/**/*',
            '/hr_attendance/static/src/xml/**/*',
        ],
        'web.assets_frontend': [
            '/portal_attendance/static/src/js/attendance_portal.js',
            '/portal_attendance/static/src/js/checkin_out.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
