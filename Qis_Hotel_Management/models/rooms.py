from odoo import fields, models, api
class RoomInfo(models.Model):
    _name = 'room.info'
    _description = 'Room Information'

    room_number = fields.Selection([
        ('F01', 'F01'),('F02', 'F02'),
        ('101', '101'),('101', '101'),
         ('201', '201'),('201', '201'),
        ('301', '301'),('302', '302'),
           ],string='F01',default='F01', required=1)
    floor_number=fields.Selection([
        ('Ground Floor', 'Ground Floor'),
        ('Floor 1', 'Floor 1'),
         ('Floor 2', 'Floor 2'),
        ('Floor 3', 'Floor 3'),
        ('Floor 4', 'Floor 4'),
           ],string='Ground Floor',default='Ground Floor')
    room_type= fields.Selection([
        ('Barchelor', 'Barchelor'),
        ('Deluxe', 'Deluxe'),
         ('Double', 'Double'),
           ],string='Room Type',default='Double')
    image= fields.Binary(string='image',required=1)


