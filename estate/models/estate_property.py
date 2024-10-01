from odoo import api,models,fields
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError
from odoo.tools.float_utils import float_is_zero, float_compare

class estate_property(models.Model):
    _name="estate.property"
    _description="The first model"

    name=fields.Char(string="Name",required=True)
    description=fields.Text(string="Description",required=True)
    postcode=fields.Char(string="Post Code",required=True)
    date_availability=fields.Date(string="Date",required=True,copy=False,default=fields.Date.add(fields.Date.today(),months=3))
    expected_price=fields.Float(string="Expected Price",required=True)
    selling_price=fields.Float(string="Selling Price",required=True,copy=False)
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
    property_type_id=fields.Integer(string="Property Id")
    tag_ids=fields.Many2many("estate.property.tag",string="Tags")
    seller=fields.Many2one('res.users', string='Seller', index=True, tracking=True, default=lambda self: self.env.user)
    buyer=fields.Many2one('res.users', string='Buyer', index=True, tracking=True, copy=False)
    offer_ids=fields.One2many("estate.property.offer","property_id")
    total_area=fields.Float(compute="_compute_total")
    best_price=fields.Float(compute="_compute_best_price")
    state=fields.Char(string="State")
    
    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            if record.offer_ids:               
                record.best_price = max(record.offer_ids.mapped('price'))
            else:
                record.best_price = 0
            
    @api.depends("living_area","garden_area")
    def _compute_total(self):
        for record in self:
            record.total_area = record.living_area+record.garden_area

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_area=10
            self.garden_orientation="north"
        else:
            self.garden_area=self.garden_orientation=False

    def action_do_sold(self):
        for record in self:
            if record.state=="Cancelled":
                raise UserError("Cancelled properties cannot be sold")
            record.state="Sold"

    def action_do_cancel(self):
        self.state="Cancelled"

    _sql_constraints=[("check_selling_price","CHECK(selling_price>0)","The selling price must be postive")]
    _sql_constraints=[("check_expected_price","CHECK(expected_price>0)","The expected price must be postive")]
    _sql_constraints=[("unique_name","UNIQUE(name)","Property Name should be unique")]

    @api.constrains('selling_price','expected_price')
    def _check_selling_price(self):
        for record in self:
            if (
                not float_is_zero(record.selling_price, precision_rounding=0.01)
                and float_compare(record.selling_price, record.expected_price * 0.9, precision_rounding=0.01) < 0
            ):
                raise ValidationError(
                    "The selling price should not be lower than 90% of the expected price! "                    
                )

    @api.ondelete(at_uninstall=False)
    def _unlink_if_new_cancelled(self):
        for record in self:
            if record.state not in ("new","Cancelled"):
                raise UserError("Only new or cancelled propert can be deleted") 

    @api.model_create_multi
    def create(self,vals_list):
        properties=super().create(vals_list)
        properties.state="Offer_Accepted"
        return properties
        
     
        
            

        
            
        
            
        
 





