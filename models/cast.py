from odoo import models, fields


class CastNetFlix(models.Model):
    _name = 'iti_netflix.movies.cast'
    _description = 'Netflix movies castes'

    name = fields.Char()
    age = fields.Date()
    address = fields.Char()
