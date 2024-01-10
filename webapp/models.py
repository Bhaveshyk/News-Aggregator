from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Prefrences(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cat = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(10000), unique=True)
    password = db.Column(db.String(1500))
    # counts = db.Column(db.Integer)
    isadmin = db.Column(db.Boolean)

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    news = db.Column(db.String(10000))
    link = db.Column(db.String(10000))
    site = db.Column(db.String(1000))
    category = db.Column(db.String(50))