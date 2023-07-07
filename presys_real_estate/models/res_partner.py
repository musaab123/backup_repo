# -*- coding: utf-8 -*-
##############################################################################
#
# odoo, Open Source Management Solution, third party addon
# Copyright (C) 2004-2015 Vertel AB (<http://vertel.se>).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

from odoo import models, fields, api, _
import odoo.tools
import logging
logger= logging.getLogger(__name__)

class res_partner(models.Model):
    _inherit = 'res.partner'
    birth_day=fields.Date(string = ' Birth Day', domain=[('is_owner', '=', True)])
    trade_name = fields.Char("Trade Name")
    commercial_egistration_No =fields.Char("Commercial Registration No")
    expiry_commercial_registration =fields.Date("Expiry Date")
    legal_agent =fields.Char("The legal agent")
    enterprise_number =fields.Char("Enterprise number")
    enterprise_name =fields.Char("Enterprise Name")
    build_number =fields.Char(" Build Number")
    branch_number =fields.Char(" Build Number")
    email_code =fields.Char(" Build Number")
    district =fields.Char(" Build Number")
    street_name =fields.Char(" Build Number")
    agency_number = fields.Char("Agency Number")
    agency_date = fields.Date("Agency Date")
    amenities_id_rel = fields.One2many('amenities.test', 'amenities_id', string=' ')


    

    # amenities_id_second = fields.Char(string="Amenities Number")
    # amenities_birth_day_second =fields.Date(string="Amenities Number")

    # amenities_id_third = fields.Char(string="Amenities Number")
    # amenities_birth_day_third =fields.Date(string="Amenities Number")


    # district =fields.Char("District")
    
    # has_group_a = fields.Boolean("show", compute='show_access_right', store=True)
    # has_group_b = fields.Boolean("show", compute='show_access_right',store=True)
    # has_group_c = fields.Boolean("show", compute='show_access_right',store=True)


    # def show_access_right(self):
    #     group_a = self.env.ref('presys_real_estate.group_a_master').users.ids
    #     group_b = self.env.ref('presys_real_estate.group_b_master').users.ids
    #     group_c = self.env.ref('presys_real_estate.group_c_master').users.ids
    #     logger.info(group_a)
    #     logger.info(group_b)
    #     logger.info(group_c)


    #     for rec in self:
    #         user_id = self.env['res.users'].sudo().search([('partner_id','=',rec.id)],limit=1).id

    #         logger.info(user_id)

    #         logger.info(rec)


    #         if (rec.user_id.id in group_a):
    #             rec.has_group_a = True
    #         else:
    #             rec.has_group_a = False

    #         if (rec.user_id.id in group_b):
    #             rec.has_group_b = True
    #         else:
    #             rec.has_group_b = False

    #         if (rec.user_id.id in group_c):
    #             rec.has_group_c = True
    #         else:
    #             rec.has_group_c = False

                




    
