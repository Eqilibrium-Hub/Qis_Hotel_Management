from odoo import fields, models, api

class PartnerInfo(models.Model):
    _name = 'partner.info'
    _description = 'Partners Information'

    business_name = fields.Char(string='Business Name')
    business_type = fields.Char(string='Business Type')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Tel Number')
    town = fields.Char(string='Town')
    province = fields.Char(string='Province')
    country = fields.Char(string='Country')

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
