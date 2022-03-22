from odoo import fields, models, api
class HotelBill(models.Model):
    _name = 'hotel.bill'
    _description = 'Hotel Bill Information'
#hotel info
    hotel_name = fields.Char(string='Hotel Name')
    address=fields.Char(string='Address')
    email= fields.Char(string='Email')
    tel=fields.Char(string='Tel Number')
#guest info
    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    phone = fields.Char(string='Phone Number')
    gender = fields.Selection([
        ('Male','Male'),
        ('Female','Female')], string='Gender',default='Male')
    town = fields.Char(string='Town')
    province= fields.Char(string='Province')
    country = fields.Char(string='Country')
#reserve details
    arrival_date = fields.Datetime(string="Arrival Date", default=fields.Datetime.now())
    dep_date = fields.Datetime(string="Departure Date", required=True)
    room_number = fields.Selection([
        ('F01', 'F01'), ('F02', 'F02'),
        ('101', '101'), ('101', '101'),
        ('201', '201'), ('201', '201'),
        ('301', '301'), ('302', '302'),
    ], string='F01', default='F01')
    resevartion_no = fields.Char(string='Reservation Number')
    price = fields.Float(string='Total Price',default=0.0)

    @api.onchange('phone')
    def onchange_validate_number(self):
        if self.phone:
            if not self.phone.strip().isdigit() or len(self.phone) != 10:
                self.phone = ''
                return {'warning':{'title':'Invalid input','message':'Please enter 10 digits Phone number'}}

    @api.onchange('email')
    def onchange_validate_email(self):
        if self.email:
            if '@' not in self.email:
                self.email = ''
                return {'warning':{'title':'Invalid input','message':'Please enter a valid email address'}}
