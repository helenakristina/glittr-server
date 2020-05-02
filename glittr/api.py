from flask import Flask
from flask_restful import Resource, Api

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

if __name__ == "__main__":
    app.run(debug=True)