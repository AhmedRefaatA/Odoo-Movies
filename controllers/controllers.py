# -*- coding: utf-8 -*-
import json
import requests
from odoo import http


class ItiNetflix(http.Controller):

    @http.route('/iti_netflix/movies/sync', auth='public', methods=['GET'])
    def sync_movies(self, **kw):
        result = http.request.env['iti_netflix.movies'].sudo()._sync_movies()
        result = {'statues': 200, 'movies_result': [movie.id for movie in result]}
        print(result)
        return json.dumps(result)

    @http.route('/iti_netflix/movies/home', auth='public', methods=['GET'])
    def index(self, **kw):
        return "Hello, world"

    @http.route('/iti_netflix/categ/list', auth='public', methods=['GET'])
    def category_index(self, **kw):
        category_objects = http.request.env['iti_netflix.movies.categories'].sudo().search([])

        print(category_objects)
        for k, v in category_objects.items():
            print(k, v)

        return json.dumps(category_objects)

    @http.route('/iti_netflix/movies/list', auth='public', methods=['GET'])
    def movies_list(self):
        movies_objs = http.request.env['iti_netflix.movies'].sudo().search([])

        movies_list = []
        for i in movies_objs:
            movies_dict = {'name': i.name, 'url': i.url if i.url else 'Doesnt exist'}
            movies_list.append(movies_dict)

        print(movies_list)
        return json.dumps(movies_list)

    @http.route('/iti_netflix/movies/create', auth='public', methods=['POST'], csrf=False)
    def movie_create_func(self, *args, **kwargs):
        print(kwargs)
        category = http.request.env['iti_netflix.movies.categories'].sudo().search(
            [('name', '=', kwargs.get('category_id'))])

        print('CATEG : ', category)

        # UPDATE DICT
        kwargs['category_id'] = category.id

        movie_obj = http.request.env['iti_netflix.movies'].sudo().create(kwargs)
        print('NEW MOVIE OBJ: ', movie_obj)
        result = {'status': 200, 'movie_id': movie_obj.id}

        return json.dumps(result)

#     @http.route('/iti_netflix/iti_netflix/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('iti_netflix.listing', {
#             'root': '/iti_netflix/iti_netflix',
#             'objects': http.request.env['iti_netflix.iti_netflix'].search([]),
#         })

#     @http.route('/iti_netflix/iti_netflix/objects/<model("iti_netflix.iti_netflix"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('iti_netflix.object', {
#             'object': obj
#         })
