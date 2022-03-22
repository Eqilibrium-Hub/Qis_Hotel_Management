from odoo import fields, models, api
import re
from odoo.exceptions import ValidationError

class GuestInfo(models.Model):
    _name = 'guest.info'
    _description = 'Guest Information'
    
    first_name = fields.Char(string='Name',required=1)
    last_name = fields.Char(string='Last Name',required=1)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone Number',required=1)
    gender = fields.Selection([
        ('Male','Male'),
        ('Female','Female')],
        string='Gender',default='Male')
    title_id= fields.Selection([
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
         ('Dr', 'Dr'),
          ('Ms', 'Ms')],string='title',default='Mr')
    town = fields.Char(string='Town')
    province= fields.Char(string='Province')
    country = fields.Char(string='Country')

    @api.onchange('phone')
    def onchange_validate_number(self):
        if self.phone:
            if not self.phone.strip().isdigit() or len(self.phone) != 10:
                self.phone = ''
                return {'warning':{'title':'Invalid input','message':'Please enter 10 digits Phone number'}}

    # @api.onchange('email')
    # def onchange_validate_email(self):
    #     if self.email:
    #         if '@' not in self.email:
    #             self.email = ''
    #             return {'warning':{'title':'Invalid input','message':'Please enter a valid email address'}}

    @api.onchange('email')
    def validate_mail(self):
        if self.email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
            if match == None:
                self.email = ''
                return {'warning':{'title':'Invalid input','message':'Not a valid E-mail ID'}}




