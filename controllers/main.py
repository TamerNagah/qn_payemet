from odoo import http
from odoo.http import request

class QNBPaymentController(http.Controller):
    @http.route(['/payment/qnb/return'], type='http', auth='public', csrf=False)
    def qnb_return(self, **post):
        # Handle the payment return
        return request.redirect('/payment/process')
