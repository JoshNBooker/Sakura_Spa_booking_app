from app import db

class Customer(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    bookings = db.relationship('Booking', backref='customer')

class Treatment(db.Model):
    __tablename__ = "treatments"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    bookings = db.relationship('Booking', backref='treatment')

class Room(db.Model):
    __tablename__ = "rooms"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    available = db.Column(db.Boolean, default = True)
    bookings = db.relationship('Booking', backref='room')

class Booking(db.Model):
    __tablename__ = "bookings"
    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    treatment_id = db.Column(db.Integer, db.ForeignKey('treatments.id'))
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))