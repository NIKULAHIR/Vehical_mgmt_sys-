# -*- coding: utf-8 -*-


{
    'name': 'Patient Managment',
    'author': 'NIKUL',
    'version': '1.1',
    'summary': 'Patient mgmt sytem',
    'sequence': 30,
    'description': " application for patient mgmt",
    'category': 'patient mgmt',

    'depends': ['base'],
    'data': ['views/patient_views.xml',
             'views/doctor_views.xml',
             'views/disease_views.xml'],
    'demo': [],
    'qweb': [],
    'application': True,
    'bootstrap': True,

    'installable': True,
    'application': True,
    'auto_install': False,
  
}
