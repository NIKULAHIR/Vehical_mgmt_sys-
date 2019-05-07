# -*- coding: utf-8 -*-

from flectra import api, fields, models

class Skill(models.Model):
    _name = "skill.data"

    name = fields.Char(size=20, string="Skill Name")