/** @odoo-module **/

import { _t } from '@web/core/l10n/translation';
import { RPCError } from "@web/core/network/rpc_service";

import paymentForm from '@payment/js/payment_form';

paymentForm.include({

    _prepareInlineForm(providerId, providerCode, paymentOptionId, paymentMethodCode, flow) {
        if (providerCode !== 'qnb') {
            this._super(...arguments);
            return;
        } else if (flow === 'token') {
            return; // Don't show the form for tokens.
        }
        this._setPaymentFlow('direct');
    },

    _initiatePaymentFlow(providerCode, paymentOptionId, paymentMethodCode, flow) {
        if (providerCode !== 'qnb' || flow === 'token') {
            this._super(...arguments); // Tokens are handled by the generic flow.
            return;
        }

        const apiKeyInput = this._getApiKeyInput();

        if (!apiKeyInput.reportValidity()) {
            this._enableButton();
            return;
        }

        this._super(...arguments);
    },

    _processDirectFlow(providerCode, paymentOptionId, paymentMethodCode, processingValues) {
        if (providerCode !== 'qnb') {
            this._super(...arguments);
            return;
        }

        const apiKeyInput = this._getApiKeyInput();
        this.rpc('/payment/qnb/process', {
            'reference': processingValues.reference,
            'api_key': apiKeyInput.value,
            'access_token': processingValues.access_token,
        }).then(() => {
            window.location = '/payment/status';
        }).catch((error) => {
            if (error instanceof RPCError) {
                this._displayErrorDialog(
                    _t("Payment processing failed"),
                    error.data.message,
                );
            } else {
                return Promise.reject(error);
            }
        });
    },

    _getApiKeyInput() {
        const radio = document.querySelector('input[name="o_payment_radio"]:checked');
        const inlineForm = this._getInlineForm(radio);
        return inlineForm?.querySelector('#o_qnb_api_key');
    },

});
