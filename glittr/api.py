from flask import Flask
from flask_restful import Resource, Api

from glittr.integrations.payment import PaymentIntent

app = Flask(__name__)
api = Api(app)


class HealthCheck(Resource):
    """Endpoint for checking health of the application
    Arguments:
        Resource {Flask-Restful Resource} -- Resource to use for routing
    """

    def get(self):
        return {"message": "okay"}


api.add_resource(HealthCheck, "/health/")
api.add_resource(PaymentIntent, "/create-payment-intent/")

if __name__ == "__main__":
    print(app)
    app.run(debug=True)
