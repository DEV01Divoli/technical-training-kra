from odoo import models,fields

class estate_property(models.Model):
    _name="estate.property"
    _description="The first model"

    name=fields.Char(string="Name",required=True)
    description=fields.Text(string="Description",required=True)
    postcode=fields.Char(string="Post Code",required=True)
    date_availability=fields.Date(string="Date",required=True)
    expected_price=fields.Float(string="Expected Price",required=True)
    selling_price=fields.Float(string="Selling Price",required=True)
    bedrooms=fields.Integer(string="No of Bedrooms",required=True)
    living_area=fields.Integer(string="Living area",required=True)
    facades=fields.Integer(string="Facades",required=True)
    garage=fields.Boolean(string="Is Garage",required=True)
    garden=fields.Boolean(string="Is Garden",required=True)
    garden_area=fields.Integer(string="Garden Area",required=True)
    garden_orientation=fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'),('east', 'East'),('west', 'West')],
        required=True)
