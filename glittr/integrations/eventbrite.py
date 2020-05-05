"""
This module contains the server-side code for pulling workshop data
from Eventbrite

"""
import json
import os

import requests
from flask import jsonify, request
from flask_restful import Resource


EVENTBRITE_API_KEY = os.environ.get('EVENTBRITE_API_KEY')


class FetchEvents(Resource):
    """Endpoint for fetching events published on Eventbrite payment

    Arguments:
        Resource {Flask-Restful Resource} -- Resource to use for routing
    """
    # todo handle errors, handle pagination, only return needed fields, store data in db
    def get(self):
        try:
            url = 'https://www.eventbriteapi.com/v3/users/me/events/'
            headers = {'Authorization': f'Bearer {EVENTBRITE_API_KEY}'}
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return jsonify(response.json())

        except Exception as e:
            return jsonify(error=str(e)), 403

