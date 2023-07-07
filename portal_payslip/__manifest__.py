# -*- coding: utf-8 -*-
# Powered by Kanak Infosystems LLP.
# © 2020 Kanak Infosystems LLP. (<https://www.kanakinfosystems.com>).

{
    'name': 'Portal Payslip Prosys',
    'version': '16.0.1.0',
    'category': 'Human Resources/Payroll',
    'summary': 'Portal Payslip using this module user can see their payslip and also down the same.| Portal Payslip | Employee Payslip | Salaryslip | Portal salaryslip | Employee Salaryslip | Portal Payslip Search | Website Employee | Website Payslip | Download Payslip.',
    'description': 'Employee can see their Payslip and also download it. Seacrh the Payslip by Date. Chat with head using chatter',
    'author': 'Kanak Infosystems LLP.',
    'website': 'https://www.kanakinfosystems.com',
    'license': 'OPL-1',
    'depends': ['hr_payroll','portal', 'portal_hr_knk','sh_hr_attendance_geolocation','hr','employee_extra_data'],
    'data': [
        'security/ir.model.access.csv',
        'views/knk_portal_payslip_views.xml',
        'report/templates/custom_header_footer.xml',
        'report/templates/real_estate_modren_template.xml',
    ],
    'images': ['static/description/banner.gif'],
    'application': True,
    'installable': True,
    'price': 60,
    'currency': 'EUR'
}
