from odoo import fields, models, api
class GuestsReviews(models.Model):
    _name = 'guest.reviews'
    _description = 'Guest Reviews'

    names = fields.Char(string='Name')
    phone = fields.Char(string='Phone Number', required=1)
    gender = fields.Selection([
        ('Male','Male'),
        ('Female','Female')], string='Gender',default='Male')
    image = fields.Binary(string='image')
    province = fields.Char(string='Province')
    country = fields.Char(string='Country')
    town = fields.Char(string='Town')
    date = fields.Datetime(string="Start Date", default=fields.Datetime.now())
    comment = fields.Text(string='Comment')

    @api.onchange('phone')
    def onchange_validate_number(self):
        if self.phone:
            if not self.phone.strip().isdigit() or len(self.phone) != 10:
                self.phone = ''
                return {'warning':{'title':'Invalid input','message':'Please enter 10 digits Phone number'}}
