from odoo import models,fields

class estate_property_type(models.Model):
    _name="estate.property.type"
    _description="Property Types"

    name=fields.Char(string="Name",required=True)
   