from odoo import models, fields, api
from datetime import date

class BookingOrder(models.Model):
    _name = 'booking.order'
    _description = 'Booking Order'

    # Fields
    booking_code = fields.Char(string="Booking Code", unique=True)
    customer_name = fields.Char(string="Customer Name", required=True)
    booking_date = fields.Date(string="Booking Date", default=date.today(), required=True)
    check_in_date = fields.Date(string="Check-in Date", required=True)
    check_out_date = fields.Date(string="Check-out Date", required=True)
    hotel_id = fields.Many2one('hotel.management', string="Hotel", required=True)
    room_type = fields.Selection([
        ('single', 'Single Bed'),
        ('double', 'Double Bed')
    ], string="Room Type", required=True)
    room_id = fields.Many2one(
        'hotel.room', string="Room ID", required=True, domain="[('hotel_id', '=', hotel_id), ('bed_type', '=', room_type), ('state', '=', 'available')]"
    )
    room_name = fields.Char(string="Room Name", related="room_id.room_code", store=True)
    state = fields.Selection([
        ('new', 'New'),
        ('confirmed', 'Confirmed')
    ], string="Booking Status", default='new', required=True)
    @api.model
    def create(self, vals):
        # Kiểm tra và tự động tạo hotel_code nếu không có
        if 'booking_code' not in vals:
            last_bill = self.search([], order='booking_code desc', limit=1)
            if last_bill:
                last_code = int(last_bill.booking_code)
                new_code = str(last_code + 1)
            else:
                new_code = '1'  # Nếu không có khách sạn nào, bắt đầu từ 1
            vals['booking_code'] = new_code

        return super(BookingOrder, self).create(vals)
    # Constraints
    @api.constrains('check_in_date', 'check_out_date')
    def _check_dates(self):
        for record in self:
            if record.check_in_date > record.check_out_date:
                raise models.ValidationError("Check-in date cannot be later than check-out date.")
    @api.depends('room_id')
    def _compute_room_code(self):
        for record in self:
            if record.room_id:
                record.room_code = record.room_id.room_code 
    # Action button
    def action_confirm_booking(self):
        for record in self:
            record.state = 'confirmed'
            record.room_id.state = 'booked'
        return {
        'type': 'ir.actions.act_window',
        'name': 'Booking Orders',
        'res_model': 'booking.order',
        'view_mode': 'list',
        'target': 'main',}
    
    def unlink(self):
        for record in self:
            if record.room_id:
                record.room_id.state = 'available'
        return super(BookingOrder, self).unlink()
