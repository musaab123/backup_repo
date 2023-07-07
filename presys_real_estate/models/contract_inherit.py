from odoo import models, fields, api, _
class contractInh(models.Model):
    _inherit = 'rental.contract'

    periodicity = fields.Selection(selection_add=[
        ('midterm', 'midterm'),
          ('quarterly', 'quarterly'),
    ], ondelete={'midterm': 'set default', 'quarterly':'set default'})
    

    



    # periodicity = fields.Selection([('days', 'Days'), ('weeks', 'Weeks'),
    #                                         ('months', 'Months'), ('years', 'Years'), ],
    #                                        string='Recurrence', required=True,
    #                                        help="Invoice automatically repeat at specified interval",
    #                                        default='months', tracking=True)