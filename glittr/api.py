from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from glittr.integrations.payment import (PaymentIntent, StripeWebhook,
                                         ChargeSavedCard)

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


api.add_resource(HealthCheck, "/health/")
api.add_resource(PaymentIntent, "/create-payment-intent/")
api.add_resource(ChargeSavedCard, "/charge-saved-card/")
api.add_resource(StripeWebhook, "/stripe-webhook/")

if __name__ == "__main__":
    print(app)
    app.run(debug=True)
