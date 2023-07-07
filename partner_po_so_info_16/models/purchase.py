# -*- coding: utf-8 -*-


from odoo import fields, models, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

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
    policy_number = fields.Char('Policy Number')
    shipping_company_name = fields.Char('Shipping Company Name')
    container_ids = fields.One2many('container.details','purchase_id',string="Containers")


    def _prepare_invoice(self):
        invoice_vals = super(PurchaseOrder, self)._prepare_invoice()
        invoice_vals['responsible_employee'] = self.responsible_employee.id
        invoice_vals['vendor_bill_number'] = self.vendor_bill_number
        invoice_vals['shipping_port'] = self.shipping_port
        invoice_vals['deliver_port'] = self.deliver_port
        invoice_vals['policy_number'] = self.policy_number
        invoice_vals['shipping_company_name'] = self.shipping_company_name
        invoice_vals['container_ids'] = [(6,0,self.container_ids.ids)]
        return invoice_vals

