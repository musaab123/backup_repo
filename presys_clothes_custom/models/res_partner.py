from odoo import models, fields, api, _
import odoo.tools

class sale_order(models.Model):
    _inherit = 'sale.order'
    customer_type = fields.Selection([('null', 'Null'),('collector', 'Collector'), ('director', 'Director'),
                                             ],
                                           string='Customer Type', required=True,
                                           default='collector')

    partner_collector_id= fields.Many2one('res.partner','Collector')
    partner_director_id= fields.Many2one('res.partner','Director')

    def action_confirm(self):
        """ Confirm the given quotation(s) and set their confirmation date.

        If the corresponding setting is enabled, also locks the Sale Order.

        :return: True
        :rtype: bool
        :raise: UserError if trying to confirm locked or cancelled SO's
        """
        if self._get_forbidden_state_confirm() & set(self.mapped('state')):
            raise UserError(_(
                "It is not allowed to confirm an order in the following states: %s",
                ", ".join(self._get_forbidden_state_confirm()),
            ))

        self.order_line._validate_analytic_distribution()

        for order in self:
            if order.partner_collector_id:
                continue
            order.message_subscribe([order.partner_collector_id.id])

        self.write(self._prepare_confirmation_values())

        # Context key 'default_name' is sometimes propagated up to here.
        # We don't need it and it creates issues in the creation of linked records.
        context = self._context.copy()
        context.pop('default_name', None)

        self.with_context(context)._action_confirm()
        if self.env.user.has_group('sale.group_auto_done_setting'):
            self.action_done()

        return True


    







    
