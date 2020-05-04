from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import getenv
from glittr.api import app

POSTGRES_URL = ''
POSTGRES_USER = ''
POSTGRES_PW = ''
POSTGRES_DB = ''

# app.config['SQLALCHEMY_DATABASE_URI'] = getenv("POSTGRES_URI")
# db = SQLAlchemy(app)