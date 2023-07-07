# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
import odoo.addons.decimal_precision as dp
from odoo.exceptions import UserError, ValidationError



class PurchaseOrder(models.Model):
    _inherit = "purchase.order"


    @api.depends('order_line.price_total', 'discount_type', 'discount_rate')
    def _amount_all(self):
        for order in self:
            if order.discount_type == 'percent':
                amount_untaxed = amount_tax  =amount_discount_rate = amount_discount = 0.0
                for line in order.order_line:
                    amount_untaxed += line.price_subtotal
                    amount_tax += line.price_tax
                    amount_discount += (line.product_uom_qty * line.price_unit * line.discount) / 100
                order.update({
                    'amount_untaxed': amount_untaxed,
                    'amount_tax': amount_tax,
                    'amount_discount': amount_discount,
                    'amount_total': amount_untaxed + amount_tax,
                })
                
            else:
                amount_untaxed = amount_tax = amount_discount_rate= amount_discount = 0.0
                for line in order.order_line:
                    amount_untaxed += line.price_subtotal
                    amount_tax += line.price_tax
                    amount_discount += (line.product_uom_qty * line.price_unit * line.discount) / 100
                    if order.discount_rate != 0 and amount_untaxed !=0:
                        amount_discount_rate = round((order.discount_rate / (amount_untaxed+amount_tax)) * 100)
                        amount_discount = amount_discount_rate * (amount_untaxed+amount_tax) / 100

                order.update({
                    'amount_untaxed': amount_untaxed,
                    'amount_tax': amount_tax,
                    'amount_discount': amount_discount,
                    'amount_total': (amount_untaxed + amount_tax) - ( (amount_untaxed + amount_tax) * amount_discount_rate / 100),
                })





    discount_type = fields.Selection([('percent', 'Percentage'), ('amount', 'Amount')], string='Discount type',
                                    readonly=False,
                                    states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
                                    default='percent')
    discount_rate = fields.Float('Discount Rate', digits=dp.get_precision('Account'),
                                readonly=False, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]})
    amount_untaxed = fields.Monetary(string='Untaxed Amount', store=True, readonly=True, compute='_amount_all',
                                    track_visibility='always')
    amount_tax = fields.Monetary(string='Taxes', store=True, readonly=True, compute='_amount_all',
                                track_visibility='always')
    amount_total = fields.Monetary(string='Total', store=True, readonly=True, compute='_amount_all',
                                track_visibility='always')
    amount_discount = fields.Monetary(string='Discount', store=True, readonly=True, compute='_amount_all',
                                    digits=dp.get_precision('Account'), track_visibility='always')

    @api.onchange('discount_type', 'discount_rate', 'order_line')
    def supply_rate(self):
        for order in self:
            if order.discount_type == 'percent':
                for line in order.order_line:
                   line.discount = order.discount_rate
            else:
                amount_untaxed = amount_tax  = amount_discount_rate = amount_discount = 0.0
                for line in order.order_line:
                    amount_untaxed += line.price_subtotal
                    amount_tax += line.price_tax
                    amount_discount += (line.product_uom_qty * line.price_unit * line.discount) / 100
                    if order.discount_rate != 0 and amount_untaxed !=0:
                        amount_discount_rate = round((order.discount_rate / (amount_untaxed+amount_tax)) * 100)
                        amount_discount = amount_discount_rate * (amount_untaxed+amount_tax) / 100

                order.update({
                    'amount_untaxed': amount_untaxed,
                    'amount_tax': amount_tax,
                    'amount_discount': amount_discount,
                    'amount_total': (amount_untaxed + amount_tax) - ( (amount_untaxed + amount_tax) * amount_discount_rate / 100),
                })

                # total = discount = 0.0
                # for line in order.order_line:
                #     total += round((line.product_qty * line.price_unit))
                # if order.discount_rate != 0:
                #     discount = (order.discount_rate / total) * 100
                # else:
                #     discount = order.discount_rate
                # for line in order.order_line:
                #     line.discount = discount

    def _prepare_invoice(self, ):
        invoice_vals = super(PurchaseOrder, self)._prepare_invoice()
        invoice_vals.update({
            'discount_type': self.discount_type,
            'discount_rate': self.discount_rate,
        })
        return invoice_vals
        

    def button_dummy(self):

        self.supply_rate()
        return True

    # @api.depends('order_line.price_total', 'discount_type', 'discount_rate')
    # def _amount_all(self):
    #     ks_res = super(PurchaseOrder, self)._amount_all()
    #     for rec in self:
    #         if not ('global_tax_rate' in rec):
    #             rec.ks_calculate_discount()
    #     return ks_res


    @api.constrains('discount_rate')
    def ks_check_discount_value(self):
        if self.discount_type == "percent":
            if self.discount_rate > 100 or self.discount_rate < 0:
                raise ValidationError('You cannot enter percentage value greater than 100.')
        else:
            if self.discount_rate < 0 or self.discount_rate > self.amount_untaxed:
                raise ValidationError(
                    'You cannot enter discount amount greater than actual cost or value lower than 0.')

    # def ks_calculate_discount(self):
    #     for rec in self:
    #         if rec.discount_type == "amount":
    #             rec.amount_discount = rec.discount_rate if rec.amount_untaxed > 0 else 0
    #         elif rec.discount_type == "percent":
    #             if rec.discount_type != 0.0:
    #                 rec.amount_discount = (rec.amount_untaxed + rec.amount_tax) * rec.discount_rate / 100
    #             else:
    #                 rec.amount_discount = 0
    #         elif not rec.discount_type:
    #             rec.amount_discount = 0
    #             rec.discount_rate = 0
    #         rec.amount_total = rec.amount_tax + rec.amount_untaxed - rec.amount_discount




class purchase_order_line(models.Model):
    _inherit = 'purchase.order.line'

    discount = fields.Float('Discount %')


    @api.depends('product_qty','discount', 'price_unit', 'taxes_id')
    def _compute_amount(self):
        for line in self:
            price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
            discount_amount = (line.price_unit * line.product_qty) * (line.discount / 100)
            
            taxes = line.taxes_id.compute_all(price, line.order_id.currency_id, line.product_qty, product=line.product_id, partner=line.order_id.partner_id)
            line.update({
                'price_tax': taxes['total_included'] - taxes['total_excluded'],
                'price_total': taxes['total_included'] ,
                'price_subtotal': taxes['total_excluded'] ,
            })

    def _prepare_compute_all_values(self):
        
        # discount = (self.price_unit * self.product_qty) * (self.discount/100)
        self.ensure_one()
        return {
            'price_unit': self.price_unit,
            # 'discount': self.discount,
            'currency': self.order_id.currency_id,
            'quantity': self.product_qty,
            'product': self.product_id,
            'partner': self.order_id.partner_id,
        }

    def _prepare_account_move_line(self, move=False):
        result = super(purchase_order_line, self)._prepare_account_move_line()
        if result:
            result.update({
                'discount' : self.discount,
            })
        return result 
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
