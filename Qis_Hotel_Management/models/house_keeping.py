from odoo import fields, models, api
class HouseKeeping(models.Model):
    _name = 'house.keeping'
    _description = 'House Keeping'

    first_name = fields.Char(string='First Name')
    phone=fields.Char(string='Phone Number')
    date = fields.Datetime(string="Date", default=fields.Datetime.now())
    room_no = fields.Char(string='Room Number')
    status = fields.Selection([
        ('Cleaned', 'Cleaned'),
        ('Not Cleaned', 'Not Cleaned')], string='Status', default='Not Cleaned')
    room_status = fields.Selection([
        ('Occupied', 'Occupied'),
        ('Not Occupied', 'Not Occupied')], string='Room Status', default='Not Occupied')

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