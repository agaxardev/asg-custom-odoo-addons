# -*- coding: utf-8 -*-
# from odoo import http


# class HrExtended(http.Controller):
#     @http.route('/hr_extended/hr_extended', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_extended/hr_extended/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_extended.listing', {
#             'root': '/hr_extended/hr_extended',
#             'objects': http.request.env['hr_extended.hr_extended'].search([]),
#         })

#     @http.route('/hr_extended/hr_extended/objects/<model("hr_extended.hr_extended"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_extended.object', {
#             'object': obj
#         })

