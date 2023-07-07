from odoo import api,fields, models, _

class res_company(models.Model):
    
    _inherit = "sale.order"
