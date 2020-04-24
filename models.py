from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False unique=True)
    password = db.Column(db.String(1000), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    contacts = db.relationship('Contact', backref='user', lazy=True, cascade='all, delete-orphan')
    interactions = db.relationship('Interaction', backref='user', lazy=True, cascade='all, delete-orphan')

class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(180), nullable=False)
    last_contacted = db.Column(db.Datetime, nullable=False, default=datetime.utcnow)
    contact_frequency = db.Column(db.Integer, nullable=False, default=180)
    interactions = db.relationship('Interaction', backref='contact', lazy=True, cascade='all, delete-orphan')

class Interaction(db.Model):
    __tablename__ = 'interactions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    conact_id = db.Column(db.Integer, db.ForeignKey('contacts.id'), nullable=False)
    timestamp = db.Column(db.Datetime, nullable=False, default=datetime.utcnow)
    method = db.Column(db.String(50), nullable=False)
    duration = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.String())
