# -*- coding: utf-8 -*-
{
    'name': "Baamtu Academy",

    'author': "Alioune Tounde Mbodj",
    'website': "http://www.baamtu.com",
    'application': True,
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security_management.xml',
        'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/classroom_views.xml',
        'views/registration_views.xml',
        'views/teacher_views.xml',
        'views/student_views.xml',
        'views/res_partner_views.xml',
        'views/registration_wizard_views.xml',
        'reports/student_registration_report.xml',
        'reports/registration_reports.xml',
        'demo/student_demo.xml',
        'demo/teacher_demo.xml',
        'demo/classroom_demo.xml',
        'demo/course_data.xml',
    ],

}
