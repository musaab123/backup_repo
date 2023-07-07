odoo.define('bi_partial_payment_invoice.account_payment',function(require){
	"use strict";

	const accountpaymentfield = require("@account/components/account_payment_field/account_payment_field");
	const { patch } = require('web.utils');
	var Dialog = require('web.Dialog');
	var core = require('web.core');
	var QWeb = core.qweb;
	var _t = core._t;
	const rpc = require('web.rpc');

	patch(accountpaymentfield.AccountPaymentField.prototype,'bi_partial_payment_invoice.account_payment', {
		async assignOutstandingCredit(id) {
			let data = await rpc.query({
                model: 'account.move',
                method: 'get_view_id',
                args: [[],["bi_partial_payment_invoice.action_payment_wizard_open"]],
            }, {
                silent: true,
            });
            var data_context = JSON.parse(data.context);
            data_context['move_id'] = this.move_id;
            data_context['line_id'] = id;

            data.context = JSON.stringify(data_context)
            
			this.action.doAction(data);
		}
	});
});












