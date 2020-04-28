from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from datetime import datetime

database_name = "keep_up_test"
database_path = "postgresql://{}:{}@{}/{}".format("postgres", "postgres", "localhost:5432", database_name)

db = SQLAlchemy()

class DatabaseItem():
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()


def setup_db(app, database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)

class User(db.Model, DatabaseItem):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    full_name = db.Column(db.String(100), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)
    contacts = db.relationship('Contact', backref='user', lazy=True, cascade='all, delete-orphan')
    interactions = db.relationship('Interaction', backref='user', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f"<User {self.id} {self.full_name} {self.email} {self.creation_date}>"

class Contact(db.Model, DatabaseItem):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(180), nullable=False)
    last_contacted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    contact_frequency = db.Column(db.Integer, nullable=False, default=180)
    interactions = db.relationship('Interaction', backref='contact', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Contact {self.id} {self.name} {self.last_contacted} {self.contact_frequency}>"

        def format(self):
            return {
                'id': self.id,
                'name': self.name,
                'last_contacted': str(self.last_contacted),
                'contact_frequency': self.contact_frequency

            }

class Interaction(db.Model, DatabaseItem):
    __tablename__ = 'interactions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    contact_id = db.Column(db.Integer, db.ForeignKey('contacts.id'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    method = db.Column(db.String(50), nullable=False)
    duration = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.String())

    def __repr__(self):
        return f"<Interaction {self.id}>"
    
    def format(self):
        return {
            'id' : self.id,
            'contact_id': self.contact_id,
            'timestamp': str(self.timestamp),
            'method': self.method,
            'durations': self.duration,
            'notes': self.notes
        }
