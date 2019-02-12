# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class RegistrationWizard (models.TransientModel):
    _name = "baamtu.academy.registration.wizard"

    def get_active_courses(self):
        return self.env['baamtu.academy.course'].browse(self._context.get('active_ids'))
        
    course_ids = fields.Many2many('baamtu.academy.course', string="Cours", default=get_active_courses)
    student_ids = fields.Many2many('baamtu.academy.student', string="etudiants")

    @api.multi
    def subscribe(self):
        for record in self:
            if record.student_ids:
                for student in record.student_ids:
                    if record.course_ids:
                        for course in record.course_ids:
                            self.env['baamtu.academy.registration'].create({'student_id': student.id, 'course_id': course.id})