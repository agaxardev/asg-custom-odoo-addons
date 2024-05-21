# -*- coding: utf-8 -*-
# from odoo import http


# class HrContractExtended(http.Controller):
#     @http.route('/hr_contract_extended/hr_contract_extended', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_contract_extended/hr_contract_extended/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_contract_extended.listing', {
#             'root': '/hr_contract_extended/hr_contract_extended',
#             'objects': http.request.env['hr_contract_extended.hr_contract_extended'].search([]),
#         })

#     @http.route('/hr_contract_extended/hr_contract_extended/objects/<model("hr_contract_extended.hr_contract_extended"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_contract_extended.object', {
#             'object': obj
#         })

