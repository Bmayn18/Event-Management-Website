from . import db
from datetime import datetime
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), index = True, nullable = False)
    firstname = db.Column(db.String(100), index = True, nullable = False)
    lastname = db.Column(db.String(100), index = True, nullable = False)
    email = db.Column(db.String(100), index = True, nullable = False)
    phone = db.Column(db.Integer, index = True, nullable = False)    
    password_hash = db.Column(db.String(255), nullable = False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))

    comments = db.relationship('Comment', backref = 'user')
    booked_events = db.relationship('Booking', backref = 'user')

class Address(db.Model):
    __tablename__ = 'address'
    id = db.Column(db.Integer, primary_key = True)
    state = db.Column(db.String(50), nullable = False)
    street = db.Column(db.String(50), nullable = False)
    suburb = db.Column(db.String(50), nullable = False)
    postcode = db.Column(db.Integer, nullable = False)
    type = db.Column(db.String(50), default = "user")

    user = db.relationship('User', backref="address")

class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key = True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    name = db.Column(db.String(100), nullable = False)
    external_link = db.Column(db.String(255))
    artist = db.Column(db.String(100), nullable = False)
    genre = db.Column(db.String(100), nullable = False)
    date = db.Column(db.Date, nullable = False)
    start_time = db.Column(db.Time, nullable = False)
    capacity = db.Column(db.Integer, nullable = False)
    ticketcount = db.Column(db.Integer, nullable = True)
    image = db.Column(db.String(400), nullable = False)
    description = db.Column(db.String(200), nullable = False)
    price = db.Column(db.String(10), nullable = False)
    status = db.Column(db.String(50), default = "open")
    venue = db.Column(db.String(50), nullable = False)

    comments = db.relationship('Comment', backref = 'event')
    bookings = db.relationship('Booking', backref = 'event')

class Booking(db.Model):
    __tablename__ = 'booking'
    id = db.Column(db.Integer, primary_key = True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    price = db.Column(db.Integer, nullable = False)
    ticket_number = db.Column(db.Integer, nullable = False)
    date_booked = db.Column(db.DateTime, default = datetime.now())

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable = False)
    text = db.Column(db.String(200), nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.now())