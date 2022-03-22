from odoo import fields, models, api
class ReservationInfo(models.Model):
    _name = 'reservation.info'
    _description = 'Reservation Information'

    first_name = fields.Char(string='First Name')
    last_name=fields.Char(string='Last Name')
    email= fields.Char(string='Email')
    phone=fields.Char(string='Phone Number')
    gender = fields.Selection([
        ('Male','Male'),
        ('Female','Female')], string='Gender',default='Male')
    country = fields.Char(string='Country')
    date_arrival = fields.Datetime(string="Arrival Date", default=fields.Datetime.now())
    date_departure = fields.Datetime(string="Departuure Date", required=True)

    room_type= fields.Selection([
        ('Single','Single'),
        ('Double','Double'),
        ('Suite','Suite')], string='Single',default='Single')
    room_number = fields.Selection([
        ('F01', 'F01'), ('F02', 'F02'),
        ('101', '101'), ('101', '101'),
        ('201', '201'), ('201', '201'),
        ('301', '301'), ('302', '302'),
    ], string='F01', default='F01')

    @api.onchange('phone')
    def onchange_validate_number(self):
        if self.phone:
            if not self.phone.strip().isdigit() or len(self.phone) != 10:
                self.phone = ''
                return {'warning': {'title': 'Invalid input', 'message': 'Please enter 10 digits Phone number'}}

    @api.onchange('email')
    def onchange_validate_email(self):
        if self.email:
            if '@' not in self.email:
                self.email = ''
                return {'warning':{'title':'Invalid input','message':'Please enter a valid email address'}}