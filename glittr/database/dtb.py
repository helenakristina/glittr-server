from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from glittr.api import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)