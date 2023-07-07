# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2022-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

from . import controllers
from . import models


def pre_install (cr):
    cr.execute(
        """update ir_model_fields set field_description ='{"ar_001":"رقم الفاتورة"}' where name ='name' and model='account.move'"""
    )


def pre_install_l (cr):
    cr.execute(
        """update ir_model_fields set field_description ='{"ar_001":"رقم الفاتورة"}' where name ='name' and model='sale.order'"""
    )
def pre_install_o(cr):
    cr.execute(
        """update ir_model_fields set field_description ='{"ar_001":"الاجمالي غير شامل الضريبة"}' where name ='amount_untaxed' and model='sale.order'"""
    )
def pre_install_u(cr):
    cr.execute(
        """update ir_model_fields set field_description ='{"ar_001":"اجمالي ضريبة القيمة المضافة"}' where name ='amount_tax' and model='sale.order'"""
    )

def pre_install_s(cr):
    cr.execute(
        """update ir_model_fields set field_description ='{"ar_001":"الاجمالي شامل الضريبة"}' where name ='amount_total' and model='sale.order'"""
    )

def pre_install_p(cr):
    cr.execute(
        """update ir_model_fields set field_description ='{"ar_001":"اسم الشريك"}' where name ='partner_id' and model='sale.order'"""
    )


def pre_install_c (cr):
    cr.execute(
        """update ir_model_fields set field_description ='{"ar_001":"الاجمالي غير شامل الضريبة"}' where name ='amount_untaxed_signed' and model='account.move'"""
    )

def pre_install_v(cr):
    cr.execute(
        """update ir_model_fields set field_description ='{"ar_001":"اسم الشريك"}' where name ='invoice_partner_display_name' and model='account.move'"""
    )

def pre_install_x(cr):
    cr.execute(
        """update ir_model_fields set field_description ='{"ar_001":"الاجمالي شامل الضريبة"}' where name ='amount_total_signed' and model='account.move'"""
    )
def pre_install_pur_1(cr):
    cr.execute(
        """update ir_model_fields set field_description ='{"ar_001":"الاجمالي غير شامل الضريبة"}' where name ='amount_untaxed' and model='purchase.order'"""
    )
def pre_install_pur_2(cr):
    cr.execute(
        """update ir_model_fields set field_description ='{"ar_001":"الاجمالي شامل الضريبة"}' where name ='amount_total' and model='purchase.order'"""
    )
# def pre_install_c (cr):
#     cr.execute(
#         "delete from ir_translation where module ='account' and src='Invoice Partner Display Name' and value ='اسم عرض شريك الفاتورة'"
#     )

# def pre_install_v (cr):
#     cr.execute(
#         "delete from ir_translation where module ='account' and src='Untaxed Amount Signed' and value ='المبلغ دون الضريبة غير موقّع '"
#     )
# def pre_install_h (cr):
#     cr.execute(
#         "delete from ir_translation where module ='account' and src='Total' and value ='الإجمالي'"
#     )

# def pre_install_a (cr):
#     cr.execute(
#         "delete from ir_translation where module ='account' and src='Total Signed' and value ='مجموع الموقّع عليهم '"
#     ) 

# def pre_install_x (cr):
#     cr.execute(
#         "delete from ir_translation where module ='account' and src='Tax ' and value ='الضريبة الموقعة '"
#     )


