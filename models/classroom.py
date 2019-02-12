# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Classroom(models.Model):
    _name = "baamtu.academy.classroom"

    name = fields.Char(string="Identifiant")
    course_ids = fields.One2many("baamtu.academy.course", "classroom_id")
    number_of_seats = fields.Integer(string="Nombres de places")