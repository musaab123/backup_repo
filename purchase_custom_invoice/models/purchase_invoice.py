from odoo import api,fields, models, _

class AmounttoWord(models.Model):

    _inherit = "purchase.order"

    def amount_to_text(self, amount,lang=None):
        self.ensure_one()
        def _num2words(number, lang):
            try:
                return num2words(number, lang=lang).title()
            except NotImplementedError:
                return num2words(number, lang='en').title()

        if num2words is None:
            logging.getLogger(__name__).warning("The library 'num2words' is missing, cannot render textual amounts.")
            return ""

        formatted = "%.{0}f".format(self.decimal_places) % amount
        parts = formatted.partition('.')
        integer_value = int(parts[0])
        fractional_value = int(parts[2] or 0)
        
        if lang:
            lang = self.env['res.lang'].search([('code','=',lang)]) or tools.get_lang(self.env)
            amount_words = tools.ustr('{amt_value} {amt_word}').format(
                        amt_value=_num2words(integer_value, lang=lang.iso_code),
                        amt_word=self.currency_unit_label,
                        )
            if not self.is_zero(amount - integer_value):
                amount_words += ' ' + _('و') + tools.ustr(' {amt_value} {amt_word}').format(
                            amt_value=_num2words(fractional_value, lang=lang.iso_code),
                            amt_word=self.currency_subunit_label,
                            )
            return amount_words
        else:
            lang = tools.get_lang(self.env)
            amount_words = tools.ustr('{amt_value} {amt_word}').format(
                        amt_value=_num2words(integer_value, lang=lang.iso_code),
                        amt_word=self.currency_unit_label,
                        )
            if not self.is_zero(amount - integer_value):
                amount_words += ' ' + _('and') + tools.ustr(' {amt_value} {amt_word}').format(
                            amt_value=_num2words(fractional_value, lang=lang.iso_code),
                            amt_word=self.currency_subunit_label,
                            )
            return amount_words
        # raise UserError(lang)





