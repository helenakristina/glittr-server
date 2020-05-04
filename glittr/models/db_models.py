from datetime import datetime

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from glittr.api import app
from glittr.database.db import db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Artist(db.Model):
    artist_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Parent(db.Model):
    parent_id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.artist_id'), nullable=False)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    children = db.relationship('Child', backref='parent')

class Child(db.Model):
    child_id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.artist_id'), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('parent.parent_id'), nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=False)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 

class Instructor(db.Model):
    instructor_id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.artist_id'), nullable=False)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 

class Workshop(db.Model):
    workshop_id = db.Column(db.Integer, primary_key=True)
    instructor_id = db.Column(db.Integer, db.ForeignKey('instructor.instructor_id'), nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey('status.status_id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    video_loc = db.Column(db.String)
    duration = db.Column(db.Integer)
    max_class_size = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    scheduled_dt = db.Column(db.DateTime, nullable=False)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    workshops = db.relationship('Workshop', backref='category')   
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 

class Workshop_child(db.Model):
    workshop_child_id = db.Column(db.Integer, primary_key=True)
    workshop_id = db.Column(db.Integer, db.ForeignKey('workshop.workshop_id'), nullable=False)
    child_id = db.Column(db.Integer, db.ForeignKey('child.child_id'), nullable=False)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Art(db.Model):
    art_id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'), nullable=False)
    art_location = db.Column(db.String, nullable=False)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Artist_art(db.Model):
    artist_art_id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.artist_id'), nullable=False)
    art_id = db.Column(db.Integer, db.ForeignKey('art.art_id'), nullable=False)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Status(db.Model):
    status_id = db.Column(db.Integer, primary_key=True)
    status_type = db.Column(db.String(20), nullable=False)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Payment_method(db.Model):
    payment_method_id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.artist_id'), nullable=False)
    stripe_customer_id = db.Column(db.String, unique= True, nullable=False)
    stripe_payment_method_id = db.Column(db.String, nullable=False)
    payment_type = db.Column(db.String(10), nullable=False)
    last_4 = db.Column(db.Integer, nullable=False)
    exp_month = db.Column(db.Integer, nullable=False)
    zip_code = db.Column(db.String, nullable=False)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Payment_instance(db.Model):
    payment_instance_id = db.Column(db.Integer, primary_key=True)
    payment_method_id = db.Column(db.Integer, db.ForeignKey('payment_method.payment_method.id'), nullable=False)
    total = db.Column(db.Float, nullable=False)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

if __name__ == '__main__':
    manager.run()