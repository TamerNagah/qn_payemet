from . import controllers
from . import models

def uninstall_hook(env):
    from odoo.addons.payment import reset_payment_provider
    reset_payment_provider(env, 'qnb')
