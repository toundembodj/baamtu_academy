# -*- coding: utf-8 -*-

from odoo import models, fields, tools, api

class RegistrationReport(models.Model):
    _name = "baamtu.academy.registration.report"
    _auto = False

    number_of_registered = fields.Integer(string="Nombre d'inscrits", readonly=True)
    course_name = fields.Char(string="Nom du cours", readonly=True)

    def _select(self):
        select_str = """
                SELECT bac.name as course_name,
                bac.id as id,
                COUNT(bar.id) as number_of_registered
        """
        return select_str

    def _group_by(self):
        group_by_str = """
                GROUP BY bac.id
        """
        return group_by_str

    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""
            CREATE view %s as
              %s
              FROM baamtu_academy_registration as bar
              INNER JOIN baamtu_academy_course as bac
                ON bac.id=bar.course_id
                %s
        """ % (self._table, self._select(), self._group_by()))
