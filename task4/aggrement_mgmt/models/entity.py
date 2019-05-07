# -*- coding: utf-8 -*-

from flectra import api, fields, models

class Entity(models.Model):
    _name = "entity.data"

    name = fields.Char(size=20, string="Entity Name")

    seller_id = fields.Many2many("seller.data","entity_seller_rel","entity_id","seller_id",string="sellers")