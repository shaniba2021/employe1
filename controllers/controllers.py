# -*- coding: utf-8 -*-
from odoo import http


class Employe1(http.Controller):
     @http.route('/employe1/employe1/', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/employe1/employe1/objects/', auth='public')
     def list(self, **kw):
         return http.request.render('employe1.listing', {
             'root': '/employe1/employe1',
             'objects': http.request.env['employe1.employe1'].search([]),
         })

     @http.route('/employe1/employe1/objects/<model("employe1.employe1"):obj>/', auth='public')
     def object(self, obj, **kw):
         return http.request.render('employe1.object', {
             'object': obj
         })
