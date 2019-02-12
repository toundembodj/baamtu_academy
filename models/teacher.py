# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Student(models.Model):
    _name = 'baamtu.academy.teacher'
    _inherits = {'res.partner': 'partner_id'}

    course_ids = fields.One2many("baamtu.academy.course", "teacher_id")
    partner_id = fields.Many2one("res.partner", required=True, ondelete="cascade")
    gender = fields.Selection([('female','Femme'), ('male','Homme')], string="Sexe")