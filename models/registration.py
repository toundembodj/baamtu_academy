# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class Registration(models.Model):
    _name = "baamtu.academy.registration"
 
    state = fields.Selection([
            ('draft', 'Brouillon'),
            ('confirmed', 'Valider'),
            ('cancelled', 'Annuler'),
            ], readonly=True, default='draft')
    date = fields.Date(string="Date d'inscription", default=fields.Date.today, readonly=True, states={'draft':[('readonly','=',False)]})
    max_reserved_places = fields.Integer(related="course_id.max_reserved_places")
    number_of_registered = fields.Integer(related="course_id.number_of_registered")
    color = fields.Integer()
    student_id = fields.Many2one("baamtu.academy.student", string="Etudiant", required=True, readonly=True, states={'draft':[('readonly','=',False)]})
    course_id = fields.Many2one("baamtu.academy.course", string="Cours", required=True, readonly=True, states={'draft':[('readonly','=',False)]})

    _sql_constraints = [('registration_unique','UNIQUE(student_id, course_id)',"Un élève ne peut s'inscrire qu'une fois à un cours !"),
    ]

    @api.constrains ('course_id')
    def _check_max_places(self):
        for record in self:
            if record.number_of_registered > record.max_reserved_places:
                raise exceptions.ValidationError("Il n'y a plus de place disponible pour ce cours !")

    @api.model
    def name_get(self):
        result = []
        for record in self:
            result.append((record.id,u"Inscription N°%s" % (record.id)))
        return result

    @api.one
    def draft_progressbar(self):
        self.write({'state': 'draft'})

    @api.one
    def validate_progressbar(self):
        self.write({'state': 'confirmed'})
        
    @api.one
    def cancel_progressbar(self):
        self.write({'state': 'cancelled'})

    @api.multi
    def unlink(self):
        if self.state not in ('draft', 'cancelled'):
            raise exceptions.ValidationError("Vous ne pouvez pas supprimé une inscription validée !")
        return super(Registration, self).unlink()
