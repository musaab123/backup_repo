# -*- coding: utf-8 -*-
from odoo import api, fields, models

class building_unit_inherit(models.Model):
    _inherit = ['product.template']
    unit_location = fields.Selection([('inside','Inside'),
                               ('outside','Outside'),
                               ], 'Unit Location',default='outside' )


    ac_type = fields.Selection([('central','Central'),
                               ('window','Window'),
                               ('aspelt','Aspelt'),

                               ], 'AC Type',default='central' )

    is_furnished = fields.Boolean( string ='Furnished')
    is_patio = fields.Boolean( string ='Patio')

    is_kitchen_cupboard = fields.Boolean( string ='kitchen cupboard')
    electricity_meter_number = fields.Char( string ='Electricity meter number')
    current_meter_reading= fields.Char( string='Current meter reading')
    gas_meter_number = fields.Char( string='Gas meter number')
    current_meter_reading_gas = fields.Char( string='Current meter reading')
    water_meter_number = fields.Char( string ='Water meter number')
    current_meter_reading_water = fields.Char( string='Current water meter reading')

    unit_number= fields.Char(string='Unit Number')
    commercial_activities = fields.Char( string="commercial activities")

    clean = fields.Boolean( string ='Cleaning')
    saft = fields.Boolean( string ='Safty')
    parking = fields.Boolean( string ='Parking')
    other = fields.Boolean( string ='Other')
    service_fees = fields.Integer(string="General service fees")
    value_deposit = fields.Integer(string="deposit Value")
    finishing_unit= fields.Selection([('scratchy','Scratchy'), ('unscratchy','Unscratchy'), ], 'Finishing')
    height = fields.Char(string=" Height")
    width = fields.Char(string=" Width")
    front = fields.Boolean( string ='Front')
    side = fields.Boolean( string ='Side')
    internal = fields.Boolean( string ='Internal')
    ac_number = fields.Char(string="AC Number")
   

class RealAccess(models.Model):
    _name = "real.access"
    _description = "Real Access"

    qui = fields.Char('Access Right',translate=True)


class ContractRealAccess(models.Model):
    _name = "contract.real.access"
    _description = "Contract Real Access"


    qui_id = fields.Many2one('real.access')
    qui_name = fields.Char(related="qui_id.qui" ,store=True,readonly=False)
    is_yes= fields.Boolean (default=False)
    contract_id = fields.Many2one('rental.contract',ondelete='cascade')

class MutualObligation(models.Model):
    _name = "mutual.obligations"
    _description = "mutual obligations"

    commitment = fields.Char('Commitment', translate=True)


class ContractMutualObligation(models.Model):
    _name = "contract.mutual.obligations"
    _description = "contract mutual obligations"

    commitment_id = fields.Many2one('mutual.obligations')
    commitment_name = fields.Char(related="commitment_id.commitment" , store=True,readonly=False)
    tenant_one = fields.Char(String='Tenant')
    lessor_one = fields.Char(String = 'Lessor')
    contract_id = fields.Many2one('rental.contract',ondelete='cascade')


class AdditionalObligations (models.Model):
    _name = "test.access"
    _description = "test access"

    commitment_qustion = fields.Char('Ask',translate=True)
 

class ContractAdditionalObligations (models.Model):
    _name = "contract.test.access"
    _description = "contract test access"

    commitment_qustion_id = fields.Many2one('test.access')
    commitment_qustion = fields.Char(related="commitment_qustion_id.commitment_qustion" , store=True,readonly=False)
    tenant_answer = fields.Char(String ='Tenant')
    lessor_answer = fields.Char( String = 'Lessor')
    contract_id = fields.Many2one('rental.contract',ondelete='cascade')


class rental_inherit(models.Model):
    _inherit = ['rental.contract']
 
    def default_get(self, default_fields):
        res = super(rental_inherit, self).default_get(default_fields)
        qustions= self.env['real.access'].search([])
        qui_lines=[]
        for q in qustions:
            qui_lines.append({'qui_id':q})
        res['admin_qustion'] = [(0, 0, vals) for vals in  qui_lines]
        mut_oblig= self.env['mutual.obligations'].search([])
        mut_oblig_lines=[]
        for q in mut_oblig:
            mut_oblig_lines.append({'commitment_id':q})
        res['mutual_obligation'] = [(0, 0, vals) for vals in  mut_oblig_lines]
        comm_qustions= self.env['test.access'].search([])
        comm_qus_lines=[]
        for q in comm_qustions:
            comm_qus_lines.append({'commitment_qustion_id':q})
        res['mutual_access'] = [(0, 0, vals) for vals in  comm_qus_lines]
        return res

    contract_time = fields.Integer(string="Contract Time")
    is_creation = fields.Boolean( string ='Creation Auto')
    is_create = fields.Boolean(string="is create")

    contract_type = fields.Selection([('commercial', 'Commercial'), ('residential', 'residential'),
                                             ],
                                           string='Contract Type', required=True,
                                           tracking=True)
    admin_qustion = fields.One2many('contract.real.access', 'contract_id',string='',required=True)
    mutual_obligation = fields.One2many('contract.mutual.obligations', 'contract_id',string='',required=True)
    mutual_access = fields.One2many('contract.test.access', 'contract_id',string='',required=True )


