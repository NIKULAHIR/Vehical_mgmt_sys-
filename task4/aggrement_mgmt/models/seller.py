# -*- coding: utf-8 -*-

from flectra import api, fields, models

class Seller(models.Model):
    _name = "seller.data"

    name = fields.Char(size=20, string="Seller Name")

    entity_ids = fields.Many2many("entity.data","entity_seller_rel",
    								"seller_id","entity_id",string="entitys")
    buyer_line = fields.One2many("buyer.data","seller_id",string="buyer")

    aggrement_data = fields.Text(string="buyers aggrement")

    state = fields.Selection([	('sc','Confirm'),
    							('pn','Pending'),
    							('rj','Rejected'),],string="States", default="pn")