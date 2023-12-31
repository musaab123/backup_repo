# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError
from odoo.tools import format_datetime, formatLang

class PricelistItem(models.Model):
    _inherit = "product.pricelist.item"
    _description = 'custom_pricelist'

# applied_on = fields.Selection(
    #     selection=[
    #         ('3_global', "All Products"),
    #         ('2_product_category', "Product Category"),
    #         ('4_product_brand', "Product Brand"),
    #         ('1_product', "Product"),
    #         ('0_product_variant', "Product Variant"),
    #         ('5_sale_persone', "Sales Teams"),

    #     ],
    #     string="Apply On",
    #     default='3_global',
    #     required=True,
    #     help="Pricelist Item applicable on selected option")

    applied_on = fields.Selection(
        selection_add=[
        ('4_product_brand', 'Product Brand'),
        ('5_sale_persone', 'Sales Teams')
        ],
        ondelete={
            '4_product_brand': 'cascade',
            '5_sale_persone': 'cascade',
        },
        )
    brand_id = fields.Many2one(
        comodel_name='product.brand',
        string="Product Brand",
        ondelete='cascade',
        help="Specify a product Brand if this rule only applies to products belonging to this brand or its children brands. Keep empty otherwise.")
    
    saleperson_id = fields.Many2one(
        comodel_name='crm.team',
        string="Sale Persone ",
        ondelete='cascade',
        help="Specify a Sale Person if this rule only applies to Persone belonging to this Sale Persone or its children Sale persone. Keep empty otherwise.")


    # === COMPUTE METHODS ===#

    @api.depends('applied_on', 'categ_id', 'brand_id','saleperson_id', 'product_tmpl_id', 'product_id', 'compute_price', 'fixed_price', \
                 'pricelist_id', 'percent_price', 'price_discount', 'price_surcharge')
    def _compute_name_and_price(self):
        for item in self:
            if item.categ_id and item.applied_on == '2_product_category':
                item.name = _("Category: %s") % (item.categ_id.display_name)
            elif item.product_tmpl_id and item.applied_on == '1_product':
                item.name = _("Product: %s") % (item.product_tmpl_id.display_name)

            elif item.brand_id and item.applied_on == '4_product_brand':
                item.name = _("Brand: %s") % (item.brand_id.display_name)
            
            elif item.saleperson_id and item.applied_on == '5_sale_persone':
                item.name = _("Sale Team: %s") % (item.saleperson_id.display_name)

            elif item.product_id and item.applied_on == '0_product_variant':
                item.name = _("Variant: %s") % (item.product_id.with_context(display_default_code=False).display_name)
            else:
                item.name = _("All Products")

            if item.compute_price == 'fixed':
                item.price = formatLang(
                    item.env, item.fixed_price, monetary=True, dp="Product Price", currency_obj=item.currency_id)
            elif item.compute_price == 'percentage':
                item.price = _("%s %% discount", item.percent_price)
            else:
                item.price = _("%(percentage)s %% discount and %(price)s surcharge", percentage=item.price_discount, price=item.price_surcharge)

            # if item.brand_id and item.applied_on == '4_product_brand':
            #     item.name = _("Brand: %s") % (item.brand_id.display_name)
            
            # elif item.saleperson_id and item.applied_on == '5_sale_persone':
            #     item.name = _("Sale Team: %s") % (item.saleperson_id.display_name)


    # === CONSTRAINT METHODS ===#
    @api.constrains('product_id', 'product_tmpl_id', 'categ_id', 'brand_id','saleperson_id')
    def _check_product_consistency(self):
        for item in self:
            if item.applied_on == "4_product_brand" and not item.brand_id:
                raise ValidationError(_("Please specify the brand for which this rule should be applied"))
            if item.applied_on == "5_sale_persone" and not item.saleperson_id:
                raise ValidationError(_("Please specify the sale Team for which this rule should be applied"))
            if item.applied_on == "2_product_category" and not item.categ_id:
                raise ValidationError(_("Please specify the category for which this rule should be applied"))
            elif item.applied_on == "1_product" and not item.product_tmpl_id:
                raise ValidationError(_("Please specify the product for which this rule should be applied"))
            elif item.applied_on == "0_product_variant" and not item.product_id:
                raise ValidationError(_("Please specify the product variant for which this rule should be applied"))

    # === ONCHANGE METHODS ===#
    @api.onchange('product_id', 'product_tmpl_id', 'categ_id', 'brand_id','saleperson_id')
    def _onchange_rule_content(self):
        if not self.user_has_groups('product.group_sale_pricelist') and not self.env.context.get('default_applied_on',
                                                                                                 False):
            # If advanced pricelists are disabled (applied_on field is not visible)
            # AND we aren't coming from a specific product template/variant.
            variants_rules = self.filtered('product_id')
            template_rules = (self - variants_rules).filtered('product_tmpl_id')
            variants_rules.update({'applied_on': '0_product_variant'})
            template_rules.update({'applied_on': '1_product'})
            (self - variants_rules - template_rules).update({'applied_on': '3_global'})



    # === CRUD METHODS ===#

    @api.model_create_multi
    def create(self, vals_list):
        for values in vals_list:
            if values.get('applied_on', False):
                # Ensure item consistency for later searches.
                applied_on = values['applied_on']
                if applied_on == '3_global':
                    values.update(dict(product_id=None, product_tmpl_id=None, categ_id=None, brand_id=None))
                elif applied_on == '2_product_category':
                    values.update(dict(product_id=None, product_tmpl_id=None))
                elif applied_on == '4_product_brand':
                    values.update(dict(product_id=None, product_tmpl_id=None))
                elif applied_on == '5_sale_persone':
                    values.update(dict(product_id=None, product_tmpl_id=None))
                elif applied_on == '1_product':
                    values.update(dict(product_id=None, categ_id=None, brand_id=None ,saleperson_id=None))
                elif applied_on == '0_product_variant':
                    values.update(dict(categ_id=None, brand_id=None,saleperson_id=None))
        return super().create(vals_list)

    def write(self, values):
        if values.get('applied_on', False):
            # Ensure item consistency for later searches.
            applied_on = values['applied_on']
            if applied_on == '3_global':
                values.update(dict(product_id=None, product_tmpl_id=None, categ_id=None, brand_id=None ,saleperson_id=None))
            elif applied_on == '2_product_category':
                values.update(dict(product_id=None, product_tmpl_id=None))
            elif applied_on == '4_product_brand':
                values.update(dict(product_id=None, product_tmpl_id=None))
            elif applied_on == '5_sale_persone':
                values.update(dict(product_id=None, product_tmpl_id=None))
            elif applied_on == '1_product':
                values.update(dict(product_id=None, categ_id=None, brand_id=None ,saleperson_id=None))
            elif applied_on == '0_product_variant':
                values.update(dict(categ_id=None, brand_id=None ,saleperson_id=None))
        return super().write(values)


    # === BUSINESS METHODS ===#

    def _is_applicable_for(self, product, qty_in_product_uom):
        """Check whether the current rule is valid for the given product & qty.

        Note: self.ensure_one()

        :param product: product record (product.product/product.template)
        :param float qty_in_product_uom: quantity, expressed in product UoM
        :returns: Whether rules is valid or not
        :rtype: bool
        """
        self.ensure_one()
        product.ensure_one()
        res = True

        is_product_template = product._name == 'product.template'
        if self.min_quantity and qty_in_product_uom < self.min_quantity:
            res = False

        elif self.brand_id:
            # Applied on a specific brand
            cat = product.brand_id
            while cat:
                if cat.id == self.brand_id.id:
                    break
            if not cat:
                res = False

        elif self.saleperson_id:
            # Applied on a specific sale Team
            res = True
            # cat = product.saleperson_id
            # while cat:
            #     if cat.id == self.saleperson_id.id:
            #         break
            # if not cat:
            #     res = False

        elif self.categ_id:
            # Applied on a specific category
            cat = product.categ_id
            while cat:
                if cat.id == self.categ_id.id:
                    break
                cat = cat.parent_id
            if not cat:
                res = False
        else:
            # Applied on a specific product template/variant
            if is_product_template:
                if self.product_tmpl_id and product.id != self.product_tmpl_id.id:
                    res = False
                elif self.product_id and not (
                        product.product_variant_count == 1
                        and product.product_variant_id.id == self.product_id.id
                ):
                    # product self acceptable on template if has only one variant
                    res = False
            else:
                if self.product_tmpl_id and product.product_tmpl_id.id != self.product_tmpl_id.id:
                    res = False
                elif self.product_id and product.id != self.product_id.id:
                    res = False

        return res



class PriceList(models.Model):
    _inherit = "product.pricelist"

    def _get_applicable_rules_domain(self, products, date, **kwargs):
        if products._name == 'product.template':
            templates_domain = ('product_tmpl_id', 'in', products.ids)
            products_domain = ('product_id.product_tmpl_id', 'in', products.ids)
        else:
            templates_domain = ('product_tmpl_id', 'in', products.product_tmpl_id.ids)
            products_domain = ('product_id', 'in', products.ids)

        return [
            ('pricelist_id', '=', self.id),
            '|', ('categ_id', '=', False), ('categ_id', 'parent_of', products.categ_id.ids),
            '|', ('brand_id', '=', False), ('brand_id', 'in', products.brand_id.ids),
            # '|', ('saleperson_id', '=', False),products_domain,
            '|', ('product_tmpl_id', '=', False), templates_domain,
            '|', ('product_id', '=', False), products_domain,
            '|', ('date_start', '=', False), ('date_start', '<=', date),
            '|', ('date_end', '=', False), ('date_end', '>=', date),
        ]