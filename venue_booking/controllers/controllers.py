from odoo import http

class VeBooking(http.Controller):

    @http.route('/home', auth='public', website=True, type='http')
    def index(self, **kw):
        try:
            print(kw['types'])

            venue = http.request.env['v.venue'].search([])

            x = http.request.env['v.slot.lines'].search([('slot_lines_venue_id', '=', int(kw['types']))]).read(['slot_lines_id'])
            print(x)
            y = http.request.env['v.slot'].search([('id', '=', tuple([x['slot_lines_id'][0] for x in x]))])
            print(y)

            slot_lines = http.request.env['v.slot.lines'].search([('slot_lines_venue_id', '=', int(kw['types']))]).read(['slot_lines_id'])
            slot = http.request.env['v.slot'].search([('id', '=', tuple([x['slot_lines_id'][0] for x in slot_lines]))])

            facilities_lines = http.request.env['v.facilities.lines'].search([('facility_lines_venue_id', '=', int(kw['types']))]).read(['facility_lines_id'])
            facilities = http.request.env['v.facilities'].search([('id', '=', tuple([x['facility_lines_id'][0] for x in facilities_lines]))])

            return http.request.render('venue_booking.home', {
                'venue': venue,
                'slot': slot,
                'facilities': facilities,
            })
        except:
            pass

        venue = http.request.env['v.venue'].search([])
        return http.request.render('venue_booking.home', {
            'venue': venue,
        })

    @http.route('/home/submit', auth='public', website=True, type='http', methods=['POST', 'GET'])
    def index_submit(self, **kw):
        print(kw)

        data = {
            'name': kw['name'],
            'phone': kw['phone'],
            'mail': kw['mail'],
            'specity': kw['specity'],
            'organization': kw['organization'],
            'venue_id': int(kw['venue_id']),
            'slot_id': int(kw['slot_id'])
        }

        http.request.env['venue.booking'].create(data)
        venue_booking_pk = [int(x) for x in list(http.request.env['venue.booking'].search([]))][-1]

        print(list([int(x) for x in list(kw['abc'].split(","))]))

        for i in list([int(x) for x in list(kw['abc'].split(","))]):
            fdata = {
                'facility_lines_id': i,
                'facility_lines_venue_id': int(kw['slot_id']),
                'facility_lines_venue_booking_id': venue_booking_pk
            }
            http.request.env['v.facilities.lines'].create(fdata)

        return 0