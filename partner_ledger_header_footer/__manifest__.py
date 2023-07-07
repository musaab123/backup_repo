# -*- coding: utf-8 -*-
##############################################################################
#
#    NCTR, Nile Center for Technology Research
#    Copyright (C) 2021-2022 NCTR (<http://www.nctr.sd>).
#
##############################################################################
{
    "name": "partner ledger report",
    "version": "1.1",
    "category": "Generic Modules/sale",
    "description": """ Manage sale module

    """,
    "author": "NCTR",
    "website": "http://www.nctr.sd",
    "depends":['account_reports','web'],
    "data": [

        # 'security/ir.model.access.csv',
        'reports/jornal_entry.xml',
        'reports/sale_header_custom.xml',
        # 'reports/jornal_entry.xml',
        # 'reports/report.xml',
    ],

    #  'assets': {
     
    #         'partner_ledger_header_footer/static/src/scss/account_report_print.scss',
      
    #  },
    "installable": True,
    "active": True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

