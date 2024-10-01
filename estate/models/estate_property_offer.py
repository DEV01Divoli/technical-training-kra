from odoo import api,models,fields
from datetime import datetime, timedelta

class estate_property_offer(models.Model):
    _name="estate.property.offer"
    _description="Property Offers"

    price=fields.Float(string="Price",required=True)
    status=fields.Selection(
        string='Status',
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')]
        )
    partner_id=fields.Many2one('res.users', string='Partner', required=True)
    property_id=fields.Many2one('estate.property')
    validity=fields.Integer(string="validity",default=7)
    date_deadline=fields.Date(string="Deadline",compute="_compute_date_deadline",inverse="_inverse_date_deadline")
    
    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for record in self:
            create_date = record.create_date.date() if record.create_date else fields.Date.today()
            record.date_deadline = fields.Date.add(create_date,days=record.validity)

    def _inverse_date_deadline(self):
        for offer in self:
            date = offer.create_date.date() if offer.create_date else fields.Date.today()
            offer.validity = (offer.date_deadline - date).days

    def action_do_accept(self):
        self.status="accepted"
        for record in self:
            record.property_id.selling_price=self.price

    def action_do_refuse(self):
        self.status="refused"

    _sql_constraints=[("check_offer_price","CHECK(price>0)","The offer price must be postive")]
           