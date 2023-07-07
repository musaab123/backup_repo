# -*- coding: utf-8 -*-
# Powered by Kanak Infosystems LLP.
# © 2020 Kanak Infosystems LLP. (<https://www.kanakinfosystems.com>).

from odoo import models


class HrPayslip(models.Model):
    _name = "hr.payslip"
    _inherit = ['portal.mixin', 'hr.payslip']

    def _compute_access_url(self):
        super(HrPayslip, self)._compute_access_url()
        for order in self:
            order.access_url = '/my/payslip/%s' % (order.id)

    def _get_move_display_name_payslip(self, show_ref=False):
        self.ensure_one()
        draft_name = ''
        if self.state == 'draft':
            draft_name += 'Draft'
            if not self.name or self.name == '/':
                draft_name += ' (* %s)' % str(self.id)
            else:
                draft_name += ' ' + self.name
        return (draft_name or self.name) + (show_ref and self.ref and ' (%s%s)' % (self.ref[:50], '...' if len(self.ref) > 50 else '') or '')

    def _get_report_base_filename(self):
        return self._get_move_display_name_payslip()
