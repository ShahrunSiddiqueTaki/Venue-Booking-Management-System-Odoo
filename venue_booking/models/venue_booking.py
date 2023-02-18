# -*- coding: utf-8 -*-
from odoo import api, fields, models
import json

# Venue Booking
class VenueBooking(models.Model):
    _name = 'venue.booking'
    _description = 'Venue Booking'

    name = fields.Char(string='Name')
    phone = fields.Char(string='Phone')
    mail = fields.Char(string='Email')

    venue_id = fields.Many2one(comodel_name='v.venue', string='Venue')
    slot_id = fields.Many2one(comodel_name='v.slot', string='Slot')
    facility_lines = fields.One2many(comodel_name='v.facilities.lines', inverse_name='facility_lines_venue_booking_id')

    @api.onchange('venue_id')
    def onchange_venue_facility(self):
        return {'domain': {'slot_id': [('id', '=', tuple([int(x) for x in list(self.venue_id.slot_lines.slot_lines_id)]))]}}

    @api.onchange('venue_id')
    def onchange_venue_slot(self):
        return {'domain': {'facility_lines': [('id', 'in', [x.id for x in self.venue_id.facility_lines])]}}

# Venue
class VVenue(models.Model):
    _name = 'v.venue'
    _description = 'Venue'

    name = fields.Char(string='Name')
    capacity = fields.Integer(string='Capacity')

    address = fields.Char(string='Address')
    contact_persion_id = fields.Many2one(comodel_name='res.partner', string='Name')
    email = fields.Char(string='Email', related='contact_persion_id.email')
    phone = fields.Char(string='Phone', related='contact_persion_id.phone')

    facility_lines = fields.One2many(comodel_name='v.facilities.lines', inverse_name='facility_lines_venue_id')
    slot_lines = fields.One2many(comodel_name='v.slot.lines', inverse_name='slot_lines_venue_id')

class VSlotLines(models.Model):
    _name = 'v.slot.lines'
    _description = 'Slot Lines'

    slot_lines_id = fields.Many2one(comodel_name='v.slot')
    slot_lines_venue_id = fields.Many2one(comodel_name='v.venue')

class VFacilitiesLines(models.Model):
    _name = 'v.facilities.lines'
    _description = 'Facilities Lines'
    _rec_name ='facility_lines_id'

    facility_lines_id = fields.Many2one(comodel_name='v.facilities')
    facility_lines_venue_id = fields.Many2one(comodel_name='v.venue')
    facility_lines_venue_booking_id = fields.Many2one(comodel_name='venue.booking')

#Slot
class VSlot(models.Model):
    _name = 'v.slot'
    _description = 'Slot'

    name = fields.Char(string='Name')
    day = fields.Selection(
        [
            ('1', 'Saturday'),
            ('2', 'Sunday'),
            ('3', 'Monday'),
            ('4', 'Tuesday'),
            ('5', 'Wednesday'),
            ('6', 'Thursday'),
            ('7', 'Friday'),
        ],
        string='Day'
    )
    date = fields.Date(string='Date')
    time = fields.Selection(
        [
            ('1', '10:00AM - 05:00PM'),
            ('2', '10:00AM - 12:00PM'),
            ('3', '12:30PM - 02:30PM'),
            ('4', '03:00PM - 05:00PM'),
        ],
        string='Time'
    )

#Facilities
class VFacilities(models.Model):
    _name = 'v.facilities'
    _description = 'Facilities'

    name = fields.Char(string='Name')
    product_id = fields.Many2one(comodel_name='product.product', string='Product')
    quantity = fields.Integer(string='Quantity')

    facilities_id = fields.Many2one(comodel_name='venue.booking', string='Venue')



