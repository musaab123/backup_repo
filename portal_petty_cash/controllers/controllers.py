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
        if request.env.user._is_admin():
            domain = []
        else:
            domain = [('employee_id', '=', request.env.user.employee_id.id)]
        if 'petty_count' in counters:
            petty_count = request.env['petty.cash'].sudo().search_count(domain) \
                if request.env['petty.cash'].sudo().check_access_rights('read', raise_exception=False) else 0
            values['petty_count'] = petty_count
        return values

    def _get_searchbar_petty_cash_inputs(self):
        return {
            'all': {'input': 'all', 'label': _('Search in All')},
            'employee': {'input': 'employee', 'label': _('Search in Employee')},
            'payment_date': {'input': 'payment_date', 'label': _('Search with payment date')},
            'type_id': {'input': 'type_id', 'label': _('Search with type_id')},
   }

    def _get_search_petty_cash_domain(self, search_in, search):
        search_domain = []
        if search_in in ('name', 'all'):
            search_domain = OR([search_domain, [('name', 'ilike', search)]])
        if search_in in ('employee', 'all'):
            search_domain = OR([search_domain, [('employee_id', 'ilike', search)]])
        if search_in in ('payment_date', 'all'):
            search_domain = OR([search_domain, [('payment_date', 'ilike', search)]])
        return search_domain

 

    def _get_searchbar_petty_cash_sortings(self):
        return {
    
            'payment_date': {'label': _('Payment Date'), 'order': 'payment_date', 'sequence': 3},
            # 'product_id': {'label': _('Category'), 'order': 'product_id', 'sequence': 4},
            # 'date': {'label': _('Date'), 'order': 'date', 'sequence': 4},

        }

    def _get_searchbar_petty_cash_groupby(self):
        values = {
            'none': {'input': 'none', 'label': _('None'), 'order': 1},
            'payment_date': {'label': _('Payment Date'), 'order': 'payment_date', 'sequence': 4},
            
        }
        # return dict(sorted(values.items(), key=lambda item: item[1]["order"]))




    def _get_groupby_petty_cash_mapping(self):
        return {
            'payment_date': 'payment_date',
            # 'date': 'date',
        }


    def _get_order(self, order, groupby):
        groupby_mapping = self._get_groupby_petty_cash_mapping()
        field_name = groupby_mapping.get(groupby, '')
        if not field_name:
            return order
        return '%s, %s' % (field_name, order)
# stop hear ---------------------------------------------------------------------------------------------------------

    @http.route(['/my/petty', '/my/petty/page/<int:page>'], type='http', auth="user", website=True)
    def portal_petty_cash(self, page=1, sortby=None, filterby=None, search=None, search_in='all', groupby=None, **kw):
        values = self._prepare_portal_layout_values()
        pettys = request.env['petty.cash'].sudo()
        _items_per_page = 20

        if request.env.user._is_admin():
            domain = []
        else:
            domain = [('employee_id', '=', request.env.user.employee_id.id)]
        searchbar_sortings = self._get_searchbar_petty_cash_sortings()
        searchbar_groupby = self._get_searchbar_petty_cash_groupby()
        searchbar_inputs = self._get_searchbar_petty_cash_inputs()
        searchbar_filters = {
            'all': {'label': _('All'), 'domain': domain},
            # 'approved': {'label': _('Approved Time Off'), 'domain': [('state', '=', 'validate')]},
            # 'to_approve': {'label': _('To Approve'), 'domain': [('state', '=', 'confirm')]},
        }

        if not sortby:
            sortby = 'payment_date'
        order = searchbar_sortings[sortby]['order']

        if not filterby:
            filterby = 'all'
        domain += searchbar_filters.get(filterby, searchbar_filters.get('all'))['domain']

        if not groupby:
            groupby = 'none'

        if search and search_in:
            domain += self._get_search_petty_cash_domain(search_in, search)

        petty_count = pettys.search_count(domain)

        pager = portal_pager(
            url="/my/petty",
            url_args={'search_in': search_in, 'search': search, 'groupby': groupby, 'filterby': filterby, 'sortby': sortby},
            total=petty_count,
            page=page,
            step=_items_per_page
        )

        order = self._get_order(order, groupby)
        pettys = pettys.search(domain, order=order, limit=_items_per_page, offset=pager['offset'])
        request.session['my_expense_history'] = pettys.ids[:100]

        groupby_mapping = self._get_groupby_petty_cash_mapping()
        group = groupby_mapping.get(groupby)
        if group:
            grouped_pettys = [petty.concat(*g) for k, g in groupbyelem(pettys, itemgetter(group))]
        else:
            grouped_pettys = [pettys]
        allocations = pettys.search([('employee_id', '=', request.env.user.employee_id.id)])
      
        values.update({
            'grouped_pettys': grouped_pettys,
            'page_name': 'petty',
            'pager': pager,
            'default_url': '/my/petty',
            'search_in': search_in,
            'search': search,
            'searchbar_sortings': searchbar_sortings,
            'searchbar_groupby': searchbar_groupby,
            'sortby': sortby,
            'groupby': groupby,
            'searchbar_inputs': searchbar_inputs,
            'searchbar_filters': OrderedDict(sorted(searchbar_filters.items())),
            'filterby': filterby,
            # 'allocations': leave_allocations,
        })
        return request.render("portal_petty_cash.portal_my_petty_cash", values)



    @http.route(['/create/petty'], type='http', auth="user", website=True)
    def petty_create(self, **post):
    # def expense_create(self, name, employee_id, product_id, date, payment_mode,total_amount,):
        employee = request.env.user.employee_id
        domain=[('state', '=', 'confirm')]
        type_id = request.env['petty.cash.type'].sudo().search(domain)
        # payment_mode = request.env['hr.expense'].sudo().search([('payment_mode','=','own_account')])
        # payment_modes = ['own_account','company_account']
        values = {
            'employee': employee,
            'type_id': type_id,
            # 'payment_modes': payment_modes,
           
        }
        return request.render("portal_petty_cash.portal_apply_petty_cash", values)


    
    @http.route(['/save/petty'], type='http', auth="user", website=True)
    def save_petty(self, **post):
        field_list = ['type_id', 'notes', 'amount', 'payment_date']
        value = []
        type_id_domain=[('state', '=', 'confirm')]
        type_id = request.env['petty.cash.type'].sudo().search(type_id_domain)
        employee = request.env.user.employee_id
        # payment_mode = request.env['hr.expense'].payment_mode
        # payment_modes = ['own_account','company_account']
        # company = request.env['res.company'].search(domain)
        # company = request.env['res.company'].search([('company_id', '=', False), ('company_id', '=', request.env.user.company_id.id)])

        for key in post:
            value.append(post[key])
            print("keeeeey",key, "vaaaaaalue", value)
        # if any([field not in post.keys() for field in field_list]) or not all(value) or not post:
        #     post.update({
        #         'employee': employee,
        #         'product_id': product_id,
        #         'payment_mode': payment_mode,
        #         'page_name': 'create_expense',
        #         'error': 'Some Required Fields are Missing.'
        #     })
        #     print("pppppppppppooooooooossssst",post)
        #     return request.render("portal_expenses.portal_apply_expense", post)


       
        vals = {
            'employee_id': request.env.user.employee_id.id,
            'type_id': post.get('type_id'),
            'payment_date': post.get('payment_date'),
            # 'company': company,
            'amount': post.get('amount'),
            'notes': post.get('notes'),

        }
        print("ooooooooooooooo",vals)
        request.env['petty.cash'].sudo().create(vals)
        return request.redirect('/my/petty')