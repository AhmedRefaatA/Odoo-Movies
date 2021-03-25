from odoo import models, fields


class NetFLixMoviesCategories(models.Model):
    _name = 'iti_netflix.movies.categories'
    _description = 'Movie Categories'

    name = fields.Char(string='Category Name')
    movies_ids = fields.One2many('iti_netflix.movies', 'category_id')
