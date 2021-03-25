from odoo import fields, models


class CustomResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    # movies_count = fields.Integer()
    movie_ids = fields.One2many('iti_netflix.movies', 'producer_id')
    my_custom_field = fields.Char()
