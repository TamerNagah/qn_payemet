from odoo import models, fields, api, _

class PaymentProviderQNB(models.Model):
    _inherit = 'payment.provider'

    provider = fields.Selection([
        ('manual', 'Manual'),
        ('transfer', 'Transfer'),
        ('qnb', 'QNB'),
    ], string="Provider", required=True, default='qnb')
    
    qnb_api_key = fields.Char(string="QNB API Key")
    qnb_api_secret = fields.Char(string="QNB API Secret")
    qnb_merchant_id = fields.Char(string="QNB Merchant ID")
    qnb_currency = fields.Selection([
        ('EGP', 'EGP'),
        ('USD', 'USD'),
    ], string="Currency", default='EGP')
    qnb_mode = fields.Selection([
        ('test', 'Test'),
        ('live', 'Live'),
    ], string="Operation Mode", default='test')
    payment_flow = fields.Selection([
        ('online', 'Online'),
        ('offline', 'Offline'),
    ], string="Payment Flow", default='online')

    @api.depends('qnb_mode')
    def _compute_payment_url(self):
        for provider in self:
            if provider.qnb_mode == 'test':
                provider.qnb_payment_url = 'https://qnbalahli.test.gateway.mastercard.com'
            else:
                provider.qnb_payment_url = 'https://qnbalahli.gateway.mastercard.com'

    def _get_supported_currencies(self):
        supported_currencies = super()._get_supported_currencies()
        if self.provider == 'qnb':
            supported_currencies = supported_currencies.filtered(lambda c: c.name in ['EGP', 'USD'])
        return supported_currencies

    def _is_tokenization_required(self, **kwargs):
        res = super()._is_tokenization_required(**kwargs)
        if self.provider == 'qnb':
            return True
        return res
