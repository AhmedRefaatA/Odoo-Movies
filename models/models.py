# -*- coding: utf-8 -*-
import requests
import json

from odoo import models, fields, api


class NetFlixMovies(models.Model):
    _name = 'iti_netflix.movies'
    _description = 'Movies ADDON'

    name = fields.Char()
    image = fields.Binary()
    url = fields.Char()
    production_year = fields.Date()
    description = fields.Html()
    subscription_price = fields.Float()

    category_id = fields.Many2one('iti_netflix.movies.categories', string='Movie Category')

    producer_id = fields.Many2one('res.partner')

    country_id = fields.Many2one('res.country')

    cast_ids = fields.Many2many('iti_netflix.movies.cast')

    def _get_my_report_name(self):
        return f'{self.name} -- {self.production_year}'

    def _sync_movies(self):
        new_ids = []
        print("INSIDE FUNCTION SYNC")
        # movies_api = 'https://'
        # synced_data = requests.get(movies_api)
        # print(synced_data)

        mediaJSON = [
            {
                "description": "Big Buck Bunny tells the story of a giant rabbit with a heart bigger than himself. When one sunny day three rodents rudely harass him, something snaps... and the rabbit ain't no bunny anymore! In the typical cartoon tradition he prepares the nasty rodents a comical revenge.\n\nLicensed under the Creative Commons Attribution license\nhttp://www.bigbuckbunny.org",
                "url": "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4",

                "name": "Big Buck Bunny2"
            },
            {"description": "The first Blender Open Movie from 2006",
             "url":
                 "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4",

             "name": "Elephant Dream2"
             },
            {
                "description": "HBO GO now works with Chromecast -- the easiest way to enjoy online video on your TV. For when you want to settle into your Iron Throne to watch the latest episodes. For $35.\nLearn how to use Chromecast with HBO GO and more at google.com/chromecast.",
                "url":
                    "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4",

                "name": "For Bigger Blazes2"
            }
        ]

        for movie in mediaJSON:
            print(f"Current Movie : \n {movie}")
            new_created_result = self.env['iti_netflix.movies'].create(movie)

            new_ids.append(new_created_result)

        return new_ids

    STATE_SELECTION = [
        ('a', 'Class A'),
        ('b', 'Class B'),
        ('c', 'Class C'),
        ('d', 'Class D'),
        ('e', 'Class E'),
    ]

    movie_class = fields.Selection(
        selection=STATE_SELECTION,
        string='Type'
    )
