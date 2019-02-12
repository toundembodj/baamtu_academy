# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Student(models.Model):
    _name = 'baamtu.academy.student'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one("res.partner", required=True, ondelete="cascade")
    registration_ids = fields.One2many("baamtu.academy.registration", "student_id", readonly=True)
    gender = fields.Selection([('female','Femme'), ('male','Homme')], string="Sexe")