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
        if 'attendance_count' in counters:
            attendance_count = request.env['hr.attendance'].sudo().search_count(domain) \
                if request.env['hr.attendance'].sudo().check_access_rights('read', raise_exception=False) else 0
            values['attendance_count'] = attendance_count
        if 'checkin_count' in counters:
            values['checkin_count'] = 0
        return values

    def _get_searchbar_attendance_inputs(self):
        return {
            'all': {'input': 'all', 'label': _('Search in All')},
            'employee': {'input': 'employee', 'label': _('Search in Employee')},
            'worked_hours': {'input': 'worked_hours', 'label': _('Search with Worked Hours')},
        }

    def _get_search_attendance_domain(self, search_in, search):
        search_domain = []
        if search_in in ('name', 'all'):
            search_domain = OR([search_domain, [('name', 'ilike', search)]])
        if search_in in ('employee', 'all'):
            search_domain = OR([search_domain, [('employee_id', 'ilike', search)]])
        if search_in in ('worked_hours', 'all'):
            search_domain = OR([search_domain, [('worked_hours', 'ilike', search)]])
        return search_domain

    def _get_searchbar_attendance_sortings(self):
        return {
            'checked_in': {'label': _('Check In'), 'order': 'check_in asc', 'sequence': 1},
            'checked_out': {'label': _('Check Out'), 'order': 'check_out asc', 'sequence': 2},
        }

    def _get_searchbar_attendance_groupby(self):
        values = {
            'none': {'input': 'none', 'label': _('None'), 'order': 1},
            'check_in': {'input': 'check_in', 'label': _('Check In'), 'order': 2},
            'check_out': {'input': 'check_out', 'label': _('Check Out'), 'order': 3},
        }
        return dict(sorted(values.items(), key=lambda item: item[1]["order"]))

    def _get_groupby_attendance_mapping(self):
        return {
            'check_in': 'check_in',
            'check_out': 'check_out',
        }

    def _get_order(self, order, groupby):
        groupby_mapping = self._get_groupby_attendance_mapping()
        field_name = groupby_mapping.get(groupby, '')
        if not field_name:
            return order
        return '%s, %s' % (field_name, order)

    @http.route(['/my/attendance', '/my/attendance/page/<int:page>'], type='http', auth="user", website=True)
    def portal_attendance(self, page=1, sortby=None, filterby=None, search=None, search_in='all', groupby=None, **kw):
        values = self._prepare_portal_layout_values()
        attendance = request.env['hr.attendance'].sudo()
        _items_per_page = 20

        if request.env.user._is_admin():
            domain = []
        else:
            domain = [('employee_id', '=', request.env.user.employee_id.id)]
        searchbar_sortings = self._get_searchbar_attendance_sortings()
        searchbar_groupby = self._get_searchbar_attendance_groupby()
        searchbar_inputs = self._get_searchbar_attendance_inputs()
        searchbar_filters = {
            'all': {'label': _('All'), 'domain': domain},
            # 'approved': {'label': _('Approved Time Off'), 'domain': [('state', '=', 'validate')]},
            # 'to_approve': {'label': _('To Approve'), 'domain': [('state', '=', 'confirm')]},
        }

        if not sortby:
            sortby = 'checked_in'
        order = searchbar_sortings[sortby]['order']

        if not filterby:
            filterby = 'all'
        domain += searchbar_filters.get(filterby, searchbar_filters.get('all'))['domain']

        if not groupby:
            groupby = 'none'

        if search and search_in:
            domain += self._get_search_attendance_domain(search_in, search)

        attendance_count = attendance.search_count(domain)

        pager = portal_pager(
            url="/my/attendance",
            url_args={'search_in': search_in, 'search': search, 'groupby': groupby, 'filterby': filterby, 'sortby': sortby},
            total=attendance_count,
            page=page,
            step=_items_per_page
        )

        order = self._get_order(order, groupby)
        attendances = attendance.search(domain, order=order, limit=_items_per_page, offset=pager['offset'])
        request.session['my_leave_history'] = attendances.ids[:100]

        groupby_mapping = self._get_groupby_attendance_mapping()
        group = groupby_mapping.get(groupby)
        if group:
            grouped_attendance = [attendance.concat(*g) for k, g in groupbyelem(attendances, itemgetter(group))]
        else:
            grouped_attendance = [attendances]

        values.update({
            'grouped_attendance': grouped_attendance,
            'page_name': 'attendance',
            'pager': pager,
            'default_url': '/my/attendance',
            'search_in': search_in,
            'search': search,
            'searchbar_sortings': searchbar_sortings,
            'searchbar_groupby': searchbar_groupby,
            'sortby': sortby,
            'groupby': groupby,
            'searchbar_inputs': searchbar_inputs,
            'searchbar_filters': OrderedDict(sorted(searchbar_filters.items())),
            'filterby': filterby,
        })
        return request.render("portal_attendance.portal_my_attendance_list", values)
    
    @http.route(['/my/check_in_attendance'], type='http', auth="user", website=True)
    def portal_check_in_out_attendance(self, page=1, sortby=None, filterby=None, search=None, search_in='all', groupby=None, **kw):
        values = self._prepare_portal_layout_values()

        _items_per_page = 20

        if request.env.user._is_admin():
            domain = []
        else:
            domain = [('employee_id', '=', request.env.user.employee_id.id)]
        searchbar_sortings = {}
        searchbar_groupby = {}
        searchbar_inputs = {}
        searchbar_filters = {
            'all': {'label': _('All'), 'domain': domain},
            # 'approved': {'label': _('Approved Time Off'), 'domain': [('state', '=', 'validate')]},
            # 'to_approve': {'label': _('To Approve'), 'domain': [('state', '=', 'confirm')]},
        }


        checkin_count = 0
        

        pager = portal_pager(
            url="/my/check_in_attendance",
            url_args={'search_in': search_in, 'search': search, 'groupby': groupby, 'filterby': filterby, 'sortby': sortby},
            total=checkin_count,
            page=page,
            step=_items_per_page
        )

        # order = self._get_order(order, groupby)
        # attendances = attendance.search(domain, order=order, limit=_items_per_page, offset=pager['offset'])
        # request.session['my_leave_history'] = attendances.ids[:100]

        # groupby_mapping = {}
        # grouped_attendance = []



        values.update({
            'page_name': '',
            'pager': pager,
            'default_url': '/my/check_in_attendance',
            'search_in': search_in,
            'search': search,
            'searchbar_sortings': {},
            'searchbar_groupby': {},
            'sortby': sortby,
            'groupby': groupby,
            'searchbar_inputs': {},
            'searchbar_filters': OrderedDict(sorted({}.items())),
            'filterby': filterby,
        })
        return request.render("portal_attendance.portal_check_in_out_attendance", values)
    
    @http.route(['/check/get_sh_attendance_manual'], type='json', auth="user",website=True)
    def get_sh_attendance_manual(self, **kw):
        employee = request.env.user.employee_id
        vals = [kw.get('message'),kw.get('latitude'),kw.get('longitude')]
        next_action = "hr_attendance.hr_attendance_action_my_attendances"
        return employee.sudo().sh_attendance_manual(vals,next_action)
    
    @http.route(['/check/get_sh_attendance_worked_time'], type='json', auth="user",website=True)
    def get_sh_attendance_worked_time(self, **kw):
        employee = request.env.user.employee_id
        if request.env['hr.attendance'].sudo().search([('employee_id','=',employee.id),('check_in','!=',False),('check_out','!=',False)], order='id desc', limit=1).check_in:
            field1 = datetime.strptime(str(request.env['hr.attendance'].sudo().search([('employee_id','=',employee.id),('check_in','!=',False),('check_out','!=',False)], order='id desc', limit=1).check_in), "%Y-%m-%d %H:%M:%S")
        else:
            return "00:00"
        if request.env['hr.attendance'].sudo().search([('employee_id','=',employee.id),('check_in','!=',False),('check_out','!=',False)], order='id desc', limit=1).check_out:
            field2 = datetime.strptime(str(request.env['hr.attendance'].sudo().search([('employee_id','=',employee.id),('check_in','!=',False),('check_out','!=',False)], order='id desc', limit=1).check_out), "%Y-%m-%d %H:%M:%S")
        else:
            return "00:00"

        # Calculate the difference between the two datetime fields
        time_diff = field2 - field1

        # Extract the time component from the timedelta object
        time_diff_in_seconds = time_diff.total_seconds()
        hours = int(time_diff_in_seconds // 3600)
        minutes = int((time_diff_in_seconds % 3600) // 60)
        seconds = int(time_diff_in_seconds % 60)
        time = "%s:%s:%s"%(str(hours).zfill(2),str(minutes).zfill(2),str(seconds).zfill(2))
        return  time
