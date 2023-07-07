from odoo import api, fields, models

class building_unit_inherit(models.Model):
    _inherit = "building"

    build_number =fields.Char(" Build Number")
    branch_number =fields.Char(" Build Number")
    email_code =fields.Char(" Build Number")
    district =fields.Char(" Build Number")
    street_name =fields.Char(" Build Number")


    instrument_number = fields.Integer("Instrument Number")
    instrument_date= fields.Date    ('Instrument Date')
    parking_number= fields.Integer ('Parking Number')
    agency_number = fields.Char("Agency Number")
    agency_date = fields.Date("Agency Date")
    agent_name= fields.Char    ('Agent Name')
    agent_phone= fields.Char ('Agent Number')
    bulding_use= fields.Char('Bulding Use')


