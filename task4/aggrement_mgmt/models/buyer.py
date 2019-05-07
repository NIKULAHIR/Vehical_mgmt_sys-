# -*- coding: utf-8 -*-

from flectra import api, fields, models

class Buyer(models.Model):
    _name = "buyer.data"

    name = fields.Char(size=20, string="Buyer Name")
    aggrement_data = fields.Text(string="sellers aggrement")

    seller_id = fields.Many2one("seller.data",string="seller")
    entity_id = fields.Many2one("entity.data",string="entity")

    state = fields.Selection([	('sc','Confirm'),
    							('pn','Pending'),
    							('rj','Rejected'),],string="States", default="pn")

    @api.onchange("seller_id")
    def onchange_buyer_data(self):
    	print("\n\n\n------id name---::", self.seller_id, self.seller_id.name)
    	self.aggrement_data = self.seller_id.aggrement_data
    	self.state = self.seller_id.state

