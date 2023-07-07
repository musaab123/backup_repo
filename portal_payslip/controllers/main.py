# -*- coding: utf-8 -*-
# Powered by Kanak Infosystems LLP.
# © 2020 Kanak Infosystems LLP. (<https://www.kanakinfosystems.com>).

from odoo import http, _
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
from odoo.http import request
from odoo.osv.expression import OR


class PayslipCount(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        if 'employee_count' in counters:
            domain = [('employee_id.user_id', '=', request.env.user.id)]
            values['employee_count'] = request.env['hr.employee'].sudo().search_count(domain)
        return values

    # def _get_searchbar_inputs(self):
    #     return {
    #         'all': {'input': 'all', 'label': _('Search in All')},
    #         'name': {'input': 'name', 'label': _('Search in Reference')},
    #         'date_from': {'input': 'date_from', 'label': _('Search in Date From')},
    #         'contract': {'input': 'contract', 'label': _('Search in Contract')},
    #         'batch': {'input': 'batch', 'label': _('Search in Batch')},
    #     }

    def _get_search_domain(self, search_in, search):
        search_domain = []
        if search_in in ('name', 'all'):
    
            return search_domain

    def _payslip_get_page_view_values(self, order, access_token, **kwargs):
        values = {
            'page_name': 'employee',
            'payslip': order,
            'token': access_token,
            'report_type': 'html',
        }
        return values

    @http.route(['/my/employee', '/my/employee/page/<int:page>'], type='http', auth="user", website=True)
    def portal_payslip(self, page=1, sortby=None, filterby=None, search=None, search_in='all', groupby=None, **kw):
        values = self._prepare_portal_layout_values()
        Emp = request.env['hr.employee']
        self._items_per_page = 10
        domain = [('employee_id.user_id', '=', request.env.user.id)]
        # searchbar_inputs = self._get_searchbar_inputs()
        if search and search_in:
            domain += self._get_search_domain(search_in, search)
        employee_count = Emp.sudo().search_count(domain)
        pager = portal_pager(
            url="/my/employee",
            url_args={'search_in': search_in, 'search': search},
            total=employee_count,
            page=page,
            step=self._items_per_page
        )
        orders = Emp.search(domain, limit=self._items_per_page, offset=pager['offset'])
        request.session['my_payslip_history'] = orders.ids[:100]
        grouped_orders = [orders]
        values.update({
            'orders': orders.sudo(),
            'grouped_orders': grouped_orders,
            'page_name': 'payslip',
            'pager': pager,
            'default_url': '/my/employee',
            'search_in': search_in,
            'search': search,
            # 'searchbar_inputs': searchbar_inputs,
        })
        return request.render("portal_payslip.portal_my_payslip_list", values)

    @http.route(['/my/employee/<int:order_id>'], type='http', auth="public", website=True)
    def portal_payslip_page(self, order_id=None, report_type=None, download=False, access_token=None, **kw):
        order_sudo = self._document_check_access('hr.employee', order_id, access_token=access_token)
        if report_type in ('html', 'pdf', 'text'):
            return self._show_report(model=order_sudo, report_type=report_type, report_ref='employee_extra_data.action_report_prosys_delevry_slip_pdf_custom', download=download)
        values = self._payslip_get_page_view_values(order_sudo, access_token, **kw)
        return request.render('portal_payslip.payslip_portal_template', values)
    



