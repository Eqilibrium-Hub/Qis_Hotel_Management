# -*- coding: utf-8 -*-
{
    'name': "QIS Hotel Management",
    'summary': """ This is a Hotel Management""",
    'description': """ This is a hotel management system, it is used to management business oprations of the hotel """,
    'author': "Nkululeko and Thabiso",
    'website': "http://www.qis.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    'category': 'management',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    # ygugugu
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/employees_info.xml',
        'views/guests_info.xml',
        'views/partners_info.xml',
        'views/rooms_info.xml',
        'views/guest_reviews.xml',
        'views/partners_info.xml',
        'views/reservation_info.xml',
        'views/hotel_bill.xml',
        'views/house_keeping.xml',
        'views/admin.xml',
        'views/house_keeper.xml',
        'views/security.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "active": False,
    'application': True,
    "sequence": 10
}
