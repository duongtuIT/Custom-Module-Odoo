from odoo import models, fields, api

class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = 'Hotel Room'

    # Fields
    hotel_id = fields.Many2one('hotel.management', string="Hotel", required=True)
    address = fields.Char(string="Hotel Address", related="hotel_id.address", store=True)
    room_code = fields.Char(string="Room Code", required=True)
    bed_type = fields.Selection([
        ('single', 'Single Bed'),
        ('double', 'Double Bed')
    ], string="Bed Type", required=True)
    price = fields.Float(string="Price", required=True)
    description = fields.Text(string="Room Features")
    state = fields.Selection([
        ('available', 'Available'),
        ('booked', 'Booked')
    ], string="Room Status", default='available', required=True)

    # Quan hệ với đặc điểm phòng
    feature_ids = fields.Many2many('room.feature', string="Room Features")

    # Ràng buộc mã phòng phải là duy nhất trong khách sạn
    _sql_constraints = [
        ('room_code_unique_per_hotel', 'unique(hotel_id, room_code)', 'Room code must be unique within a hotel.')
    ]
    