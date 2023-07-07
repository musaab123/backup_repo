# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import models, fields, _, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    def _get_employee_related(self):
        employee = self.env['hr.employee'].search([('user_id','=',self.env.user.id)])
        if employee:
            return employee.id
        else:
            return False

    part_id = fields.Char('Partner ID',related='partner_id.partner_id',store=True)
    vendor_bill_number = fields.Char('Vendor Bill Number')
    responsible_employee = fields.Many2one('hr.employee','Responsible Employee',default=_get_employee_related)
    shipping_port = fields.Char('Shipping Port')
    deliver_port = fields.Char('Deliver Port')
    from_city = fields.Many2one('res.country.state','From City')
    to_city = fields.Many2one('res.country.state','to City')
    distributer_name = fields.Char('Distributer Name')
    distributer_car_number = fields.Char('Distributer Car Number')
    policy_number = fields.Char('Policy Number')
    shipping_company_name = fields.Char('Shipping Company Name')
    container_ids = fields.One2many('container.details','account_id',string="Containers")