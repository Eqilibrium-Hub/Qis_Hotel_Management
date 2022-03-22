from odoo import fields, models, api


class ReportInfo(models.Model):
    _name = 'report.info'
    _description = 'Report Information'

    Receptionist_name = fields.Char(string='Names')
    arrival_date = fields.Datetime(string="Arrival Date", default=fields.Datetime.now())

    bill_no = fields.Char(string='Bill Number')
    guest_name = fields.Char(string='Guest Name')
    nationality = fields.Char(string='Nationality')
    room_number = fields.Selection([
        ('F01', 'F01'), ('F02', 'F02'),
        ('101', '101'), ('101', '101'),
        ('201', '201'), ('201', '201'),
        ('301', '301'), ('302', '302'),
    ], string='F01', default='F01')
    days_spent = fields.Char(string='Number of days')
    total_amount=fields.Float(string='Total Amount Paid', default=0.0)
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