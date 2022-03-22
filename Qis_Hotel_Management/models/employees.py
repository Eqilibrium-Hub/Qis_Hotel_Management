from odoo import fields, models, api
class EmployeesInfo(models.Model):
    _name = 'employee.info'
    _description = 'Employee Information'

    first_name = fields.Char(string='First Name',required=1)
    last_name = fields.Char(string='Last Name',required=1)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone Number',required=1)
    gender = fields.Selection([
        ('Male','Male'),
        ('Female','Female')], string='Gender',default='Male')
    department= fields.Selection([
        ('Cleaning', 'Cleaning'),
        ('HR', 'HR'),
         ('ADMIN', 'ADMIN'),
          ('SECURITY', 'SECURITY')],string='Department',default='Admin')
    image= fields.Binary(string='image')
    town = fields.Char(string='Town')
    province= fields.Char(string='Province')
    country = fields.Char(string='Country')

class Admin(models.Model):
    _name = 'admin.info'
    _description = 'Admin Information'

    first_name = fields.Char(string='First Name',required=1)
    last_name = fields.Char(string='Last Name',required=1)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone Number',required=1)
    gender = fields.Selection([
    ('Male', 'Male'),
    ('Female', 'Female')], string='Gender', default='Male')
    image = fields.Binary(string='image')
    town = fields.Char(string='Town')
    province = fields.Char(string='Province')
    country = fields.Char(string='Country')

class Security(models.Model):
    _name = 'security.info'
    _description = 'Security Information'

    first_name = fields.Char(string='First Name',required=1)
    last_name = fields.Char(string='Last Name',required=1)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone Number',required=1)
    gender = fields.Selection([
          ('Male', 'Male'),
          ('Female', 'Female')], string='Gender', default='Male')
    image = fields.Binary(string='image')
    town = fields.Char(string='Town')
    province = fields.Char(string='Province')
    country = fields.Char(string='Country')


class HouseKeeper(models.Model):
    _name = 'house.keeper'
    _description = 'HouseKeeper Information'

    first_name = fields.Char(string='First Name',required=1)
    last_name = fields.Char(string='Last Name',required=1)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone Number',required=1)
    gender = fields.Selection([
        ('Male', 'Male'),
        ('Female', 'Female')], string='Gender', default='Male')
    image = fields.Binary(string='image')
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
