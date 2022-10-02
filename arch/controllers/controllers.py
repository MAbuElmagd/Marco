# -*- coding: utf-8 -*-
# from odoo import http


# class Arch(http.Controller):
#     @http.route('/arch/arch', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/arch/arch/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('arch.listing', {
#             'root': '/arch/arch',
#             'objects': http.request.env['arch.arch'].search([]),
#         })

#     @http.route('/arch/arch/objects/<model("arch.arch"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('arch.object', {
#             'object': obj
#         })
