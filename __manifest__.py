{
    'name': "Payment Provider: QNB Gateway",
    'version': '1.0',
    'category': 'Accounting/Accounting',
    'icon': '/payment_qnb/static/src/img/qnb_logo.png',  # تأكد من وجود الأيقونة في المسار الصحيح
    'summary': "A payment provider for QNB in Egypt.",
    'author': "Tamer Nagah Elsayed",
    'website': "https://tn-system.com",
    'depends': ['payment', 'account_payment','payment_custom', 'website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/payment_provider_views.xml',
        'views/payment_qnb_templates.xml',
        'data/payment_provider_data.xml',
        'data/ir_cron.xml',
        'data/mail_template_data.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'payment_qnb/static/src/js/payment_form.js',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
