from odoo import models,fields

class estate_property(models.Model):
    _name="estate.property"
    _description="The first model"

    name=fields.Char(string="Name",required=True)
    description=fields.Text(string="Description",required=True)
    postcode=fields.Char(string="Post Code",required=True)
    date_availability=fields.Date(string="Date",required=True,copy=False,default=fields.Date.add(fields.Date.today(),months=3))
    expected_price=fields.Float(string="Expected Price",required=True)
    selling_price=fields.Float(string="Selling Price",required=True,readonly=True,copy=False,default=150)
    bedrooms=fields.Integer(string="No of Bedrooms",required=True,default=2)
    living_area=fields.Integer(string="Living area",required=True)
    facades=fields.Integer(string="Facades",required=True)
    garage=fields.Boolean(string="Is Garage",required=True)
    garden=fields.Boolean(string="Is Garden",required=True)
    garden_area=fields.Integer(string="Garden Area",required=True)
    status=fields.Boolean(default=True)
    garden_orientation=fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'),('east', 'East'),('west', 'West')],
        required=True)
    property_old=fields.Selection(string='Property Age',selection=[('old','Old'),('medium','Medium'),('new','Newly Built')],required=True,default="new")
    
