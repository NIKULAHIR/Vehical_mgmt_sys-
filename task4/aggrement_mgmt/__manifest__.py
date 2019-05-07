# -*- coding: utf-8 -*-


{
    'name': 'Aggrement Managment System',
    'author': 'NIKUL',
    'version': '1.1',
    'summary': 'Aggrement mgmt sytem',
    'sequence': 30,
    'description': " application for Aggrement mgmt",
    'category': 'Aggrement mgmt',

    'depends': ['base'],
    'data': [
        'views/seller_data.xml',
        'views/buyer_data.xml',
        'views/entity_data.xml'
    ],
    'demo': [],
    'qweb': [],
    'application': True,
    'bootstrap': True,

    'installable': True,
    'application': True,
    'auto_install': False,

}
