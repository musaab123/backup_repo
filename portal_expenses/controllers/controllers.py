# -*- coding: utf-8 -*-
# Powered by Kanak Infosystems LLP.
# © 2020 Kanak Infosystems LLP. (<https://www.kanakinfosystems.com>).

from odoo import http, _
from operator import itemgetter
from pytz import timezone, UTC
from odoo.addons.resource.models.resource import float_to_time
from collections import OrderedDict
from collections import namedtuple
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
from odoo.http import request
from odoo.osv.expression import OR
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF
from datetime import datetime
from odoo.tools import groupby as groupbyelem

DummyAttendance = namedtuple('DummyAttendance', 'hour_from, hour_to, dayofweek, day_period, week_type')


class PortalAttendanceKnk(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        
        domain = [('name', '=', request.env.user.name)]
       
        certificate_count = request.env['hr.employee'].sudo().search_count(domain) 
              
        values['certificate_count'] = certificate_count
        return values
    


        #   if request.env.user._is_admin():
        #     domain = []
        # else:
        #     domain = [('employee_id', '=', request.env.user.employee_id.id)]

        # if 'certificate_count' in counters:
        #     certificate_count = request.env['hr.employee'].sudo().search()  \
        #         if request.env['hr.employee'].sudo().check_access_rights('read', raise_exception=False) else 0
        #     values['certificate_count'] = certificate_count
        # if 'certificate_count' in counters:
        #     values['certificate_count'] = 0
        # return values



    @http.route(['/my/certificate', '/my/certificate/page/<int:page>'], type='http', auth="user", website=True)
    def portal_certificate(self, **kw):
        # values = self._prepare_portal_layout_values()
        sertificate_obj = request.env['hr.employee'].sudo()
        domain = [('name', '=', request.env.user.name)]
        serificate = sertificate_obj.search(domain)
        vals = {'serificate':serificate ,'page_name':'certificate_list_view'}
  
        return request.render("portal_expenses.portal_my_certificate_list", vals)


    @http.route(['/my/certificates/<model("hr.employee"):employee_id>'], type='http', auth="user", website=True)
    def portal_certificate_form(self, employee_id , **kw):
        vals = {"employee":employee_id}
  
        return request.render("portal_expenses.payslip_portal_template", vals)
    
    @http.route(['/my/certificates/print/<model("hr.employee"):employee_id>'], type='http', auth="user", website=True)
    def portal_certificate_print(self, employee_id , **kw):
  
        return self._show_report(model=employee_id, report_type='pdf', report_ref='employee_extra_data.delevry_slip_pdf_custom', download=True)
    
    @http.route(['/my/salary/print/<model("hr.employee"):employee_id>'], type='http', auth="user", website=True)
    def portal_certificate_print_custom(self, employee_id , **kw):
  
        return self._show_report(model=employee_id, report_type='pdf', report_ref='employee_extra_data.sallary_certifcate_pdf_custom', download=True)

   



   