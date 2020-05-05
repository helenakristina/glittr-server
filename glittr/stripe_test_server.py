# serve.py

from flask import Flask
from flask import render_template

# creates a Flask application, named app
app = Flask(__name__)


# a route where we will display a welcome message via an HTML template
@app.route("/checkout/")
def hello():
    return render_template('checkout.html')

# run the application
if __name__ == "__main__":
    app.run(debug=True, port=4242)