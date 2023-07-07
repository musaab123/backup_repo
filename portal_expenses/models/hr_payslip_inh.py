# -*- coding: utf-8 -*-
# Powered by Kanak Infosystems LLP.
# © 2020 Kanak Infosystems LLP. (<https://www.kanakinfosystems.com>).

from odoo import models


class HrEmployee(models.Model):
    _name = "hr.employee"

    def _get_report_base_filename(self):
        return self.name
