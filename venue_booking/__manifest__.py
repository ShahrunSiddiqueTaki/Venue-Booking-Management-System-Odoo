# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Venue Booking System',
    'category': 'Booking System',
    'summary': 'Venue Booking System',
    'description': "Venue Booking System",
    'version': '15.0.0',
    'sequence': -1,
    'depends': [
        'base',
        'stock',
        'contacts',
        'website',
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/v_wizard.xml',
        'reports/report_template_2.xml',
        'reports/report_template.xml',
        'views/venue_booking_view.xml',
        'views/menu.xml',
        'views/website_menu.xml',
        'views/templates.xml',
     ],
    # 'assets': {
    #     # 'web.assets_backend': [
    #     #     ('include', 'venue_booking/static/src/css/web_assets_backend.css'),
    #     #     ('include', 'venue_booking/static/src/js/web_assets_backend.js'),
    #     # ],
    #     'web.assets_frontend': [
    #         # ('include', 'venue_booking/static/src/css/web_assets_frontend.css'),
    #         'venue_booking/static/src/js/web_assets_frontend.js',
    #     ],
    #     # 'web.assets_common': [
    #     #     # ('include', 'venue_booking/static/src/css/web_assets_common.css'),
    #     #     'venue_booking/static/src/js/web_assets_common.js'
    #     # ],
    # },
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
    'assets': {},
}
