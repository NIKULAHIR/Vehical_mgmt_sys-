# -*- coding: utf-8 -*-

from flectra import api, fields, models

class Jobs(models.Model):
    _name = "jobs.data"

    name = fields.Char(size=20, string="job Name")