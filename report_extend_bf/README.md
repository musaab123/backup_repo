* REQUIREMENTS *
  Install:
    - py3o.template (0.9.9 or better) An easy solution to design reports using LibreOffice, for basic templating (odt->odt and ods->ods only)
    - genshi (0.7 or better)
    - Unoconv: Convert files to any format that supports LibreOffice. Website: http://dag.wiee.rs/home-made/unoconv/
      Download
      The following packages (in order of appearance) are available.
        Red Hat 
        Debian
        Fedora
        Mandriva
        Ubuntu Lucid
        OpenSUSE


  LibreOffice (Versión: 4.4.6.3 or better). tested with LibreOffice write versión: 4.4.6.3 (Optional for create templates)


Supported output format combinations (Template -> Output):
  odt -> odt(default) odt -> pdf odt -> doc odt -> docx odt -> pds

Note:
  If the program unoconv default output will show in ODT format regardless of the output field you selected in the report is not installed.

Extend and personalize object report example:
  #Object extend
  class sale_oder(models.Model):
      _inherit = "sale.order"

      #Use method
      def custom_report(self):
          obj_precision = self.env['decimal.precision']
          prec = obj_precision.precision_get('Account')
          lines = []
          for item in self.order_line:
              lines.append(
                  {"product": item.name,
                   "qty": int(item.product_uom_qty),
                   "image": item.product_id.image_medium,
                   "price_unit": format(item.price_unit, '.%sf' % prec),
                   "tax": ', '.join(map(lambda x: (x.description or x.name), item.tax_id)),
                   "price_subtotal": format(item.price_subtotal, '.%sf' % prec),
                   })
          values = {
              "order_line": lines,
              "untaxed": format(self.amount_untaxed, '.%sf' % prec),
              "tax": format(self.amount_tax, '.%sf' % prec),
              "total": format(self.amount_total, '.%sf' % prec),
              "symbol": self.pricelist_id.currency_id.symbol
          }
          #Return Dict
          return values

Define field value in document:
  py3o.data.total
  py3o.data.untaxed
  py3o.data.tax

