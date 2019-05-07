# -*- coding: utf-8 -*-
from flectra import api, fields, models

class DoctorData(models.Model):
    _name="doctor.data"

    name = fields.Char(string="doctor Name")
    appoimnt_date = fields.Date(string="available on", required=True)
    disease_ids = fields.Many2many("disease.data", "disease_doctore_rel", "doctore_id", "disease_id", string="specialist_on")
    patient_line = fields.One2many("patient.data", "doctore_id", string="patient name",)
    state = fields.Selection([('sc','success'),
                                    ('pn','pending'),
                                    ('rj','rejected')], string="status", default="sc")
    
    def state_pending(self):
        self.state = "pn"
   
    def state_rejected(self):
        self.state = 'rj'

    def state_confirm(self):
        self.state = 'sc'


  