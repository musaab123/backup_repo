# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import models, fields, _, api

GENDER_SELECTION = [('male', 'Male'), ('female', 'Female')]


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    def mail_reminder(self):
        """Documents expiry date notification"""

        now = datetime.now() + timedelta(days=1)
        date_now = now.date()
        match = self.search([])
        for i in match:
            if i.id_expiry_date:
                exp_date = fields.Date.from_string(i.id_expiry_date) - timedelta(days=14)
                if date_now >= exp_date:
                    mail_content = "  Hello  " + i.name + ",<br>Your ID " + i.identification_id + "is going to expire on " + \
                                   str(i.id_expiry_date) + ". Please renew it before expiry date"
                    main_content = {
                        'subject': _('ID-%s Expired On %s') % (i.identification_id, i.id_expiry_date),
                        'author_id': self.env.user.partner_id.id,
                        'body_html': mail_content,
                        'email_to': i.work_email,
                    }
                    self.env['mail.mail'].sudo().create(main_content).send()
        match1 = self.search([])
        for i in match1:
            if i.passport_expiry_date:
                exp_date1 = fields.Date.from_string(i.passport_expiry_date) - timedelta(days=180)
                if date_now >= exp_date1:
                    mail_content = "  Hello  " + i.name + ",<br>Your Passport " + i.passport_id + "is going to expire on " + \
                                   str(i.passport_expiry_date) + ". Please renew it before expiry date"
                    main_content = {
                        'subject': _('Passport-%s Expired On %s') % (i.passport_id, i.passport_expiry_date),
                        'author_id': self.env.user.partner_id.id,
                        'body_html': mail_content,
                        'email_to': i.work_email,
                    }
                    self.env['mail.mail'].sudo().create(main_content).send()

    personal_mobile = fields.Char(string='Mobile', related='address_home_id.mobile', store=True,
                  help="Personal mobile number of the employee")
    joining_date = fields.Date(string='Joining Date', help="Employee joining date computed from the contract start date",compute='compute_joining', store=True)
    id_expiry_date = fields.Date(string='Expiry Date', help='Expiry date of Identification ID')
    passport_expiry_date = fields.Date(string='Expiry Date', help='Expiry date of Passport ID')
    id_attachment_id = fields.Many2many('ir.attachment', 'id_attachment_rel', 'id_ref', 'attach_ref',
                                        string="Attachment", help='You can attach the copy of your Id')
    passport_attachment_id = fields.Many2many('ir.attachment', 'passport_attachment_rel', 'passport_ref', 'attach_ref1',
                                              string="Attachment",
                                              help='You can attach the copy of Passport')
    fam_ids = fields.One2many('hr.employee.dependents', 'employee_id', string='Dependents', help='Dependents Information')

    @api.depends('contract_id')
    def compute_joining(self):
        if self.contract_id:
            date = min(self.contract_id.mapped('date_start'))
            self.joining_date = date
        else:
            self.joining_date = False

    # @api.onchange('spouse_complete_name', 'spouse_birthdate')
    # def onchange_spouse(self):
    #     relation = self.env.ref('employee_info_ksa_16.employee_relationship')
    #     lines_info = []
    #     spouse_name = self.spouse_complete_name
    #     date = self.spouse_birthdate
    #     iqama = self.spouse_iqama
    #     if spouse_name and date:
    #         lines_info.append((0, 0, {
    #             'member_name': spouse_name,
    #             'relation_id': relation.id,
    #             'birth_date': date,
    #             'iqama_id':spouse_iqama,
    #         })
    #                           )
    #         self.fam_ids = [(6, 0, 0)] + lines_info



    @api.onchange('spouse_complete_name', 'spouse_birthdate')
    def onchange_spouse(self):
        relation = self.env.ref('ent_hr_employee_updation.employee_relationship')
        if self.spouse_complete_name and self.spouse_birthdate:
            self.fam_ids = [(0, 0, {
                'member_name': self.spouse_complete_name,
                'relation_id': relation.id,
                'birth_date': self.spouse_birthdate,
            })]

class HrEmployeeDependentsInfo(models.Model):
    """employee dependents information"""
    _name = 'hr.employee.dependents'
    _description = 'HR Employee Dependents'

    employee_id = fields.Many2one('hr.employee', string="Employee", help='Select corresponding Employee',
                                  invisible=1)
    relation_id = fields.Many2one('hr.employee.relation', string="Relation", help="Relationship with the employee")
    member_name = fields.Char(string='Name')
    member_contact = fields.Char(string='Contact No')
    birth_date = fields.Date(string="DOB", tracking=True)
    iqama_id = fields.Integer(string="National/Iqama ID")



class EmployeeRelationInfo(models.Model):
    """employee dependents information"""

    _name = 'hr.employee.relation'

    name = fields.Char(string="Relationship", help="Relationship with thw employee")
