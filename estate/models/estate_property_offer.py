from odoo import fields, models
from datetime import timedelta

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate property offer'

    price = fields.Float()
    status = fields.Selection(selection=[('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)
    partner_id = fields.Many2one('res.partner', 'Partner', required=True)
    property_id = fields.Many2one('estate.property', 'Property', required=True)
    validity = fields.Integer(
        default=7
    )
    date_deadline = fields.Date(

    )
