# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'V Booking',
    'category': 'Booking System',
    'summary': 'Venue Booking System',
    'description': "Venue Booking System",
    'version': '15.0.0',
    'sequence': -2,
    'depends': [
        'base',
        'stock',
        'contacts',
        'venue_booking',
    ],
    'data': [
        # 'security/ir.model.access.csv',
        # 'wizard/v_wizard.xml',
        # 'reports/report_template_2.xml',
        # 'reports/report_template.xml',
        'views/v_booking_view.xml',
        # 'views/menu.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
    'assets': {},
}
