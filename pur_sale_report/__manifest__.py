# -*- coding: utf-8 -*-
##############################################################################
#
#    NCTR, Nile Center for Technology Research
#    Copyright (C) 2021-2022 NCTR (<http://www.nctr.sd>).
#
##############################################################################
{
    "name": "prosys purchase management",
    "version": "1.1",
    "category": "Generic Modules/sale",
    "description": """ Manage sale module

    """,
    "author": "NCTR",
    "website": "http://www.nctr.sd",
    "depends":['sale','web'],
    "data": [

        # 'security/ir.model.access.csv',
        'reports/sale_header_custom.xml',
        'reports/jornal_entry.xml',
        'reports/report.xml',

        
        

    
    ],
    "installable": True,
    "active": True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

