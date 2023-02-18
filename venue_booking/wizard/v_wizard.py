# -*- coding: utf-8 -*-
from odoo import api, fields, models

class VWizard(models.TransientModel):
    _name = 'v.wizard'
    _description = 'Create Report'

    name = fields.Many2one(string='Name', comodel_name='res.partner')
    mail = fields.Char(string='Email', related='name.email')
    phone = fields.Char(string='Phone', related='name.phone')

    def action_print_report(self):
        print(self.read()[0])
        data = {
            'form': self.read()[0]
        }
        # return self.env.ref('venue_booking.first_report').with_context(landscape=True).report_action(self, data=data)
        return self.env.ref('venue_booking.action_report').report_action(self, data=data)


