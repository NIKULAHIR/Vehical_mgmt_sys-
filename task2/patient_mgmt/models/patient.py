# -*- coding: utf-8 -*-
from flectra import api, fields, models

class PatientData(models.Model):
    _name="patient.data"

    name = fields.Char(string="Patient Name", size=20)
    address= fields.Text(string="Patient Addres")
    appoimnt_date = fields.Date(string="appoiment ", readonly=True,)
    disease = fields.Many2one("disease.data", string="select disease")

    doctore_id = fields.Many2one("doctor.data", string="Approved ")
    state = fields.Selection([('sc','success'),
                                    ('pn','pending'),
                                    ('rj','rejected')], string="status", default="sc")

    @api.onchange("doctore_id")
    def onchange_store_data(self):
    	
        print("---------------patient / name, ID /----------------", self.name, self.doctore_id)
        self.appoimnt_date = self.doctore_id.appoimnt_date
        self.state = self.doctore_id.state
        
        