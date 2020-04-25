from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from datetime import datetime

database_name = "keep_up_test"
database_path = "postgresql://{}:{}@{}/{}".format("postgres", "postgres", "localhost:5432", database_name)

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    migrate = Migrate(app, db)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    full_name = db.Column(db.String(100), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)
    contacts = db.relationship('Contact', backref='user', lazy=True, cascade='all, delete-orphan')
    interactions = db.relationship('Interaction', backref='user', lazy=True, cascade='all, delete-orphan')

class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.auth_id'), nullable=False)
    name = db.Column(db.String(180), nullable=False)
    last_contacted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    contact_frequency = db.Column(db.Integer, nullable=False, default=180)
    interactions = db.relationship('Interaction', backref='contact', lazy=True, cascade='all, delete-orphan')

class Interaction(db.Model):
    __tablename__ = 'interactions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.auth_id'), nullable=False)
    conact_id = db.Column(db.Integer, db.ForeignKey('contacts.id'), nullable=False)
    timestamp = db.Column(db.DateTme, nullable=False, default=datetime.utcnow)
    method = db.Column(db.String(50), nullable=False)
    duration = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.String())
