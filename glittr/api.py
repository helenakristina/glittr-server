from os import getenv

from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from glittr.database.db import get_artist, add_artist
from glittr.integrations.payment import PaymentIntent, ChargeSavedCard, StripeWebhook

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)



# Sets the 'Access-Control-Allow-Origin' header on the response to avoid
# Stripe creating CORS error from server & client being on different domains
# TODO enable credential’ed requests & add ensure CSRF protection
CORS(app)

class HealthCheck(Resource):
    """Endpoint for checking health of the application
    Arguments:
        Resource {Flask-Restful Resource} -- Resource to use for routing
    """

    def get(self):
        return {"message": "okay"}


class ArtistEndpoint(Resource):
    def get(self, artist_id):
        return get_artist(artist_id, app)
        
    def put(self, artist_id):
        artist = request.json
        return artist

    def delete(self, artist_id):
        pass


class CreateArtistEndpoint(Resource):
    def post(self):
        artist = request.json

        # TODO validate input
        artist_id = add_artist(artist, app)
        return {"artist": artist_id}


api.add_resource(HealthCheck, "/health/")
api.add_resource(PaymentIntent, "/create-payment-intent/")
api.add_resource(ArtistEndpoint, "/artist/<int:artist_id>")
api.add_resource(CreateArtistEndpoint, "/artist/")

api.add_resource(ChargeSavedCard, "/charge-saved-card/")
api.add_resource(StripeWebhook, "/stripe-webhook/")

if __name__ == "__main__":
    print(app)
    app.run(debug=True)
