# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import models, fields, _, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _get_employee_related(self):
        employee = self.env['hr.employee'].search([('user_id','=',self.env.user.id)])
        if employee:
            return employee.id
        else:
            return False

    part_id = fields.Char('Partner ID',related='partner_id.partner_id',store=True)
    responsible_employee = fields.Many2one('hr.employee','Responsible Employee',default=_get_employee_related)
    shipping_port = fields.Char('Shipping Port')
    deliver_port = fields.Char('Deliver Port')
    from_city = fields.Many2one('res.country.state','From City')
    to_city = fields.Many2one('res.country.state','to City')
    distributer_name = fields.Char('Distributer Name')
    distributer_car_number = fields.Char('Distributer Car Number')
    policy_number = fields.Char('Policy Number')
    shipping_company_name = fields.Char('Shipping Company Name')
    container_ids = fields.One2many('container.details','sale_id',string="Containers")

    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['responsible_employee'] = self.responsible_employee.id
        invoice_vals['shipping_port'] = self.shipping_port
        invoice_vals['deliver_port'] = self.deliver_port
        invoice_vals['from_city'] = self.from_city.id
        invoice_vals['to_city'] = self.to_city.id
        invoice_vals['distributer_name'] = self.distributer_name
        invoice_vals['distributer_car_number'] = self.distributer_car_number
        invoice_vals['policy_number'] = self.policy_number
        invoice_vals['shipping_company_name'] = self.shipping_company_name
        invoice_vals['container_ids'] = [(6,0,self.container_ids.ids)]
        return invoice_vals




class Containers(models.Model):
    _name = 'container.details'
    _rec_name = 'container_number'

    sale_id = fields.Many2one('sale.order','Sale Order')
    purchase_id = fields.Many2one('purchase.order','Purchase Order')
    account_id = fields.Many2one('account.move','Accounts')
    container_number = fields.Char('Container Number')
    container_weight = fields.Char('Container weight')
    container_size = fields.Char('Container Size')
    cbm = fields.Char('CBM')




class StockPicking(models.Model):
    _inherit = 'stock.picking'

    invoice_id = fields.Many2one('account.move','Invoice Number')
    container_ids = fields.One2many('container.details','sale_id',string="Containers" , compute="_get_questions")


    def _get_questions(self):
            self.container_ids = self.env['container.details'].search([])




