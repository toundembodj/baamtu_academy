# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class Courses(models.Model):
    _name = 'baamtu.academy.course'

    name = fields.Char(string="Nom", required=True)
    code = fields.Char(string="Code", compute="_compute_code")
    max_reserved_places = fields.Integer(string="Nombre maximum de places", required=True)
    date_start = fields.Date(string="Date de début", required=True)
    date_stop = fields.Date(string="Date de fin", required=True)
    category = fields.Selection([('computer_science', 'Informatique'),
                                ('accounting', 'Comptabilité')], 
                                string="Catégorie", required=True)
    description = fields.Text(string="Description")
    active = fields.Boolean(string="Actif", default=True)
    color = fields.Integer() #for keeping color index on Kanban view
    number_of_registered = fields.Integer(compute="_compute_number_registered", string="Nombre d'inscrits", store=True)
    is_registered = fields.Boolean(compute="_compute_registered", string="Inscrits")
    classroom_id = fields.Many2one("baamtu.academy.classroom", string="Salle de classe")
    teacher_id = fields.Many2one("baamtu.academy.teacher", string="Professeur")
    registration_ids = fields.One2many("baamtu.academy.registration", "course_id")

    @api.multi
    @api.onchange('name')
    def _compute_code(self):
        for record in self:
            record.code = "REF_C_{}".format(record.id)
        return record.code

    @api.multi
    @api.depends('registration_ids')
    def _compute_registered(self):
        for record in self:
            if record.registration_ids:
                record.is_registered = True
            else:
                record.is_registered = False

    @api.multi
    @api.depends('registration_ids')
    def _compute_number_registered(self):
        for record in self:
            counter = self.env['baamtu.academy.registration'].search_count([('course_id','=',record.id)])
            record.number_of_registered = counter

    @api.constrains ('max_reserved_places')
    def _check_places_against_registered(self):
        for record in self:
            if record.number_of_registered > record.max_reserved_places:
                raise exceptions.ValidationError("Veuillez augmenter le nombre de places car {} étudiants sont inscrits!".format(record.number_of_registered))