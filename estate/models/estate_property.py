# -*- coding: utf-8 -*-

from odoo import api, fields, models
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
    salesperson_id = fields.Many2one(
        'res.users',
        string='Salesperson',
        index=True,
        default=lambda self: self.env.user
    )
    buyer_id = fields.Many2one('res.partner', string='Buyer', index=True)
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string="Offers")
    total_area = fields.Float(compute="_compute_total_area")
    best_offer = fields.Float(compute="_max_offer")

    @api.depends('garden_area', 'living_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.garden_area + record.living_area

    @api.depends('offer_ids')
    def _max_offer(self):
        for record in self:
            offer_prices = record.offer_ids.mapped('price')
            record.best_offer = max(offer_prices) if len(offer_prices) != 0 else None
