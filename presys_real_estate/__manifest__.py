# -*- coding: utf-8 -*-
{
    'name':'Real Estate Custom',
    'version':'1.0',
    'category':'Real Estate Custom',
    'sequence':14,
    'summary':'',
    'description':""" Real Estate Management""",
    'author':'Presys',
    'depends':['itsys_real_estate','account'],
    'data':[
        'security/real_estate_security.xml',
        'security/ir.model.access.csv',
        # 'security/ir.rule.xml',
        # t-if="env.user.partner_id.has_group_a"
        'views/unit_inherit.xml',
        'views/proerty_inherit.xml',
        'views/res_partner.xml',
        'views/rental_contract.xml',
        'views/access_configration.xml',
        'report/templates/rental_contract.xml',
        'report/templates/commercial_contract_report.xml',
        'report/templates/custom_header_footer.xml',
        'report/templates/real_estate_modren_template.xml',


        'report/report_menu.xml',




    ],
    'images': ['static/description/images/splash-screen.jpg'],
    'installable':True,
    'auto_install':False,
    'currency': 'EUR',
    'price': 600,
    'application':True,
    'license': "AGPL-3",
}