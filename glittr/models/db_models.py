from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from glittr.api import app

# probably put in the api file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Parent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # foreign key
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 


class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # foreign key
    date_of_birth = db.Column(db.DateTime, nullable=False)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 

class Parent_child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # foreign key child
    # foreign key parent
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 

class Instructor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # foreign key artist
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 

class Workshop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # foreign key instructor
    # foreign key status
    scheduled_datetime = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text, nullable=False)
    video_loc = db.Column(db.String)
    duration = db.Column(db.Integer)
    max_class_size = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 

class Workshop_category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # foreign key workshop
    # foreign key category
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 

class Workshop_child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # foreign key workshop
    # foreign key child
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Art(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # foreign key category
    # max length for art_location?
    art_location = db.Column(db.String, nullable=False)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Artist_art(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # artist foreign key
    # art_id foreign key
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status_type = db.Column(db.String(20), nullable=False)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Payment_method(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # artist id foreign key
    # max len for stripe_customer_id??
    stripe_customer_id = db.Column(db.String, unique= True, nullable=False)
    stripe_payment_method_id = db.Column(db.String, nullable=False)
    payment_type = db.Column(db.String(10), nullable=False)
    # way to limit to 4?
    last_4 = db.Column(db.Integer, nullable=False)
    exp_month = db.Column(db.Integer, nullable=False)
    zip_code = db.Column(db.String)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Payment_instance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # payment method foroeign key
    total = db.Column(db.Float, nullable=False)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)