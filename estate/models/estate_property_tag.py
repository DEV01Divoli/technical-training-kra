from odoo import models,fields

class estate_property_tag(models.Model):
    _name="estate.property.tag"
    _description="Property Tags"

    name=fields.Char(string="Name",required=True)
    
    _sql_constraints=[("unique_name","UNIQUE(name)","Tag Name should be unique")]
   