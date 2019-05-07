# -*- coding: utf-8 -*-

from flectra import api, fields, models

class JobSeeker(models.Model):
    _name = "job.seeker"

    name = fields.Char(size=20, string="job seeker Name")