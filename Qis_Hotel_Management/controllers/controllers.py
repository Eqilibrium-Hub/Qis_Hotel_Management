# -*- coding: utf-8 -*-
# from odoo import http


# class QisHotelBooking(http.Controller):
#     @http.route('/qis_hotel_management/qis_hotel_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/qis_hotel_management/qis_hotel_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('qis_hotel_management.listing', {
#             'root': '/qis_hotel_management/qis_hotel_management',
#             'objects': http.request.env['qis_hotel_management.qis_hotel_management'].search([]),
#         })

#     @http.route('/qis_hotel_management/qis_hotel_management/objects/<model("qis_hotel_management.qis_hotel_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('qis_hotel_management.object', {
#             'object': obj
#         })
