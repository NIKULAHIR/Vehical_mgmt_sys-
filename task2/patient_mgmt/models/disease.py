# -*- coding: utf-8 -*-
from flectra import api, fields, models

class DieaseData(models.Model):
    _name="disease.data"

    name = fields.Selection([('T1D','Type 1 Diabetes'),
                             ('MS','Multiple Sclerosis'),
                             ('UC','Crohns & Colitis'),
                             ('lupus','Lupus'),
                             ('type-5','rheumatoid-arth'),
                             ('type-6','Allergies & Asthma'),
                             ('type-7','Celiac Disease'),
                             ('type-8','Relapsing Polychondritis'),
                             ('type-9','Liver Disease'),
                             ('type-10','Infectious Diseases'),
                             ], string="Disease Name",)
    discription = fields.Text(string="Disease description")
    image = fields.Binary(string="Symbol")
    doctore_ids = fields.Many2many("doctor.data","disease_doctore_rel","disease_id", "doctore_id" ,string="doctore")

    