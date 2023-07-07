# -*- coding: utf-8 -*-
##############################################################################
#
#    NCTR, Nile Center for Technology Research
#    Copyright (C) 2021-2022 NCTR (<http://www.nctr.sd>).
#
##############################################################################
{
    "name": "Design reports for sales, purchases and accounts",
    "version": "1.1",
    "category": "Generic Modules/sale",
    "description": """ Manage Reports for the management of purchases, 
            sales, accounting, stores, and extracting the stock 
            bond upon receipt and shipment

    """,
    "author": "NCTR",
    "website": "http://www.nctr.sd",
    "depends":['sale','account','stock','purchase','partner_po_so_info_16','bi_sale_purchase_discount_with_tax'],
    "data": [

        # 'security/ir.model.access.csv',
        'security/group_company_employee.xml',

        'reports/sale_header_custom.xml',
        'reports/jornal_entry.xml',
        'reports/modren_invoice_template.xml',
        'reports/purchase_modren_template.xml',
        'reports/Invoice_services_to_supplier.xml',
        'reports/delevry_slip_custom.xml',
        'reports/invoice_utility_bill.xml',
        'reports/report.xml',
        'reports/ksa_sale_order_template.xml',
        'reports/ksa_header_footer_custom.xml',
        'reports/ksa_invoice_sale_custom.xml',
        'reports/ksa_purchase_order_template.xml',
        'reports/ksa_invoice_purchase_custom.xml',
        'reports/ksa_invoice_service_to_supplier.xml',
        'reports/ksa_invoice_utility.xml',
        'reports/ksa_delevry_slip_purchase.xml',
        'reports/ksa_delevery_slip_sale.xml',
        'views/res_company_view.xml',


        
        

    
    ],
    "installable": True,
    "active": True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

