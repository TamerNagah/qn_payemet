from odoo import models, fields, api

class PaymentProviderQNB(models.Model):
    _inherit = 'payment.provider'

    provider = fields.Selection(selection_add=[('qnb', 'QNB')], ondelete={'qnb': 'set default'})
    qnb_api_key = fields.Char(string="QNB API Key", required=True)
    qnb_api_secret = fields.Char(string="QNB API Secret", required=True)
    qnb_merchant_id = fields.Char(string="QNB Merchant ID", required=True)
    qnb_currency = fields.Selection([
        ('EGP', 'EGP'),
        ('USD', 'USD'),
    ], string="Currency", default='EGP', required=True)
    qnb_mode = fields.Selection([
        ('test', 'Test'),
        ('live', 'Live'),
    ], string="Operation Mode", default='test', required=True)
    qnb_payment_url = fields.Char(string="Payment URL", compute='_compute_payment_url')

    @api.depends('qnb_mode')
    def _compute_payment_url(self):
        for provider in self:
            if provider.qnb_mode == 'test':
                provider.qnb_payment_url = 'https://qnbalahli.test.gateway.mastercard.com'
            else:
                provider.qnb_payment_url = 'https://qnbalahli.gateway.mastercard.com'

    def _qnb_get_api_credentials(self):
        """ Retrieve API credentials based on the selected mode """
        return {
            'merchant_id': self.qnb_merchant_id,
            'api_key': self.qnb_api_key,
            'api_secret': self.qnb_api_secret,
        }
