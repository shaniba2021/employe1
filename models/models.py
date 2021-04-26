# -*- coding: utf-8 -*-

from odoo import models, fields, api


class employe1(models.Model):
     _name = 'employe1.employee'
     _description = 'employe1.employe'

     name = fields.Char( 'name')
     age= fields.Integer('age')
     gender = fields.Selection([('g1', 'Male') , ('d2', 'Female')] , 'Gender')
     phone = fields.Integer('Mobile Number')
     dept= fields.Char('department')

     
     
 class department(models.Model):
    _name = 'employe1.department'
    _description = 'employe1.employe'
     
     name = fields.Char( 'name')
    age= fields.Integer('age')
    gender = fields.Selection([('g1', 'Male') , ('d2', 'Female')] , 'Gender')
    phone = fields.Integer('Mobile Number')
    dept= fields.Char('department')
     
