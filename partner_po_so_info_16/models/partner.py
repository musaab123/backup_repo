from odoo.exceptions import Warning
from odoo import models, fields, api, _


class Partner(models.Model):
    _inherit = 'res.partner'

    partner_id = fields.Char('Partner ID')
    wechat_id = fields.Char('Wechat')

    _sql_constraints = [
        ('partner_id_uniq',
         'unique (partner_id)',
         'Partner ID should be unique.')
    ]
