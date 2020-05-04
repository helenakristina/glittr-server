from datetime import datetime

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from glittr.api import app
from glittr.database.dtb import db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
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
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    children = db.relationship('Child', backref='parent')

class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'), nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=False)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 

# class Parent_child(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     child_id = db.Column(db.Integer, db.ForeignKey('child.id'), nullable=False)
#     parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'), nullable=False)
#     inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 

class Instructor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 

class Workshop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    instructor_id = db.Column(db.Integer, db.ForeignKey('instructor.id'), nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    video_loc = db.Column(db.String)
    duration = db.Column(db.Integer)
    max_class_size = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    scheduled_dt = db.Column(db.DateTime, nullable=False)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workshops = db.relationship('Workshop', backref='category')   
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 

# class Workshop_category(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     workship_id = db.Column(db.Integer, db.ForeignKey('workshop.id'), nullable=False)
#     category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
#     inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 

class Workshop_child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workshop_id = db.Column(db.Integer, db.ForeignKey('workshop.id'), nullable=False)
    child_id = db.Column(db.Integer, db.ForeignKey('child.id'), nullable=False)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Art(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    art_location = db.Column(db.String, nullable=False)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Artist_art(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    art_id = db.Column(db.Integer, db.ForeignKey('art.id'), nullable=False)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status_type = db.Column(db.String(20), nullable=False)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Payment_method(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    stripe_customer_id = db.Column(db.String, unique= True, nullable=False)
    stripe_payment_method_id = db.Column(db.String, nullable=False)
    payment_type = db.Column(db.String(10), nullable=False)
    last_4 = db.Column(db.Integer, nullable=False)
    exp_month = db.Column(db.Integer, nullable=False)
    zip_code = db.Column(db.String, nullable=False)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Payment_instance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    payment_method_id = db.Column(db.Integer, db.ForeignKey('payment_method.id'), nullable=False)
    total = db.Column(db.Float, nullable=False)
    inserted_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

if __name__ == '__main__':
    manager.run()