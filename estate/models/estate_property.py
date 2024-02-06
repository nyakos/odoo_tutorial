# -*- coding: utf-8 -*-

from odoo import fields, models
from datetime import timedelta


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property Model'

    name = fields.Char(
        required=True
    )
    postcode = fields.Char()
    date_availability = fields.Date(
        default=fields.Datetime.today() + timedelta(days=90),
        copy=False
    )
    expected_price = fields.Float(
        required=True
    )
    selling_price = fields.Float(
        readonly=True
    )
    bedrooms = fields.Integer(
        default=2
    )

    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Garden Orientation', selection=[
            ('north', 'North'), ('east', 'East'), ('south', 'South'), ('west', 'West')
        ],
        help='Which direction the garden is orientated'
    )
    active = fields.Boolean(
        default=True
    )
    state = fields.Selection(
        string='State', selection=[
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('canceled', 'Canceled'),
        ],
        default='new',
        help='Which direction the garden is orientated'
    )
    property_type_id = fields.Many2one("estate.property.type", string="Type")

