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
        if 'payslip_count' in counters:
            domain = [('employee_id.user_id', '=', request.env.user.id)]
            values['payslip_count'] = request.env['hr.payslip'].sudo().search_count(domain)
        return values

    def _get_searchbar_inputs(self):
        return {
            'all': {'input': 'all', 'label': _('Search in All')},
            'name': {'input': 'name', 'label': _('Search in Reference')},
            'date_from': {'input': 'date_from', 'label': _('Search in Date From')},
            'contract': {'input': 'contract', 'label': _('Search in Contract')},
            'batch': {'input': 'batch', 'label': _('Search in Batch')},
        }

    def _get_search_domain(self, search_in, search):
        search_domain = []
        if search_in in ('name', 'all'):
            search_domain = OR([search_domain, [('name', 'ilike', search)]])
        if search_in in ('date_from', 'all'):
            search_domain = OR([search_domain, [('date_from', 'ilike', search)]])
        if search_in in ('contract', 'all'):
            search_domain = OR([search_domain, [('contract_id', 'ilike', search)]])
        if search_in in ('batch', 'all'):
            search_domain = OR([search_domain, [('payslip_run_id', 'ilike', search)]])
        return search_domain

    def _payslip_get_page_view_values(self, order, access_token, **kwargs):
        values = {
            'page_name': 'payslip',
            'payslip': order,
            'token': access_token,
            'report_type': 'html',
        }
        return values

    @http.route(['/my/payslip', '/my/payslip/page/<int:page>'], type='http', auth="user", website=True)
    def portal_payslip(self, page=1, sortby=None, filterby=None, search=None, search_in='all', groupby=None, **kw):
        values = self._prepare_portal_layout_values()
        PaySlip = request.env['hr.payslip']
        self._items_per_page = 10
        domain = [('employee_id.user_id', '=', request.env.user.id)]
        searchbar_inputs = self._get_searchbar_inputs()
        if search and search_in:
            domain += self._get_search_domain(search_in, search)
        payslip_count = PaySlip.sudo().search_count(domain)
        pager = portal_pager(
            url="/my/payslip",
            url_args={'search_in': search_in, 'search': search},
            total=payslip_count,
            page=page,
            step=self._items_per_page
        )
        orders = PaySlip.search(domain, limit=self._items_per_page, offset=pager['offset'])
        request.session['my_payslip_history'] = orders.ids[:100]
        grouped_orders = [orders]
        values.update({
            'orders': orders.sudo(),
            'grouped_orders': grouped_orders,
            'page_name': 'payslip',
            'pager': pager,
            'default_url': '/my/payslip',
            'search_in': search_in,
            'search': search,
            'searchbar_inputs': searchbar_inputs,
        })
        return request.render("portal_payslip_knk.portal_my_payslip_list", values)

    @http.route(['/my/payslip/<int:order_id>'], type='http', auth="public", website=True)
    def portal_payslip_page(self, order_id=None, report_type=None, download=False, access_token=None, **kw):
        order_sudo = self._document_check_access('hr.payslip', order_id, access_token=access_token)
        if report_type in ('html', 'pdf', 'text'):
            return self._show_report(model=order_sudo, report_type=report_type, report_ref='hr_payroll.action_report_payslip', download=download)
        values = self._payslip_get_page_view_values(order_sudo, access_token, **kw)
        return request.render('portal_payslip_knk.payslip_portal_template', values)
