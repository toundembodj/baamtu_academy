# -*- coding: utf-8 -*-

from odoo.tests import common
import logging

my_logger = logging.getLogger(__name__)

class TestCourse(common.TransactionCase):

    def test_course(self):
        course_env = self.env['baamtu.academy.classroom'].create({'name':'Salle_10'})
        self.assertEqual(course_env.name,'Salle_0' )
