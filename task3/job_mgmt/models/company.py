# -*- coding: utf-8 -*-

from flectra import api, fields, models

class Company(models.Model):
    _name = "company.data"

    name = fields.Char(size=20, string="Company Name")