# -*- coding: utf-8 -*-

from odoo.tests import common

class TestClassroom(common.TransactionCase):

    def test_course(self):
        course_env = self.env['baamtu.academy.classroom'].create({'name':'Salle'})
        self.assertEqual(course_env.name, 'Salle1')
