# -*- coding: utf-8 -*-


{
    'name': 'Job Managment',
    'author': 'NIKUL',
    'version': '1.1',
    'summary': 'Job mgmt sytem',
    'sequence': 30,
    'description': " application for job mgmt",
    'category': 'Job mgmt',

    'depends': ['base'],
    'data': ['views/company_data_view.xml',
             'views/skill_data_view.xml',
             'views/job_seeker_data_view.xml',
             'views/jobs_data_view.xml'],
    'demo': [],
    'qweb': [],
    'application': True,
    'bootstrap': True,

    'installable': True,
    'application': True,
    'auto_install': False,

}
