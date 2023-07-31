from flask import Flask, render_template, redirect, Blueprint, request
from app import db
from models import Customer, Treatment, Booking,Room
from datetime import datetime, timedelta

booking_blueprint = Blueprint('booking',__name__)

# HOME

@booking_blueprint.route('/')
def home_page():
    return render_template('index.jinja', title = 'Sakura Spa')

# BOOKINGS

@booking_blueprint.route('/bookings')
def display_bookings():
    bookings = Booking.query.all()
    customers = Customer.query.all()
    return render_template('bookings/diary.jinja', bookings=bookings, customers=customers)

@booking_blueprint.route('/bookings', methods=["POST"])
def submit_new_booking():
    date_time = request.form["date_time"]
    customer_id = request.form["customer"]
    treatment_id = request.form["treatment"]
    new_booking = Booking(date_time = date_time,customer_id = customer_id,treatment_id = treatment_id)
    for b in Booking.query.all():
        actual_date_time = date_time[0:10] + " " + date_time[11:16]
        difference = datetime.strptime(actual_date_time, "%Y-%m-%d %H:%M") - b.date_time
        two_hours = timedelta(hours=2)
        if difference >= two_hours:
            print("all good")
    db.session.add(new_booking)
    db.session.commit()
    return redirect('/bookings')

@booking_blueprint.route('/bookings/<id>')
def show_customers_bookings(id):
    bookings = Booking.query.filter_by(customer_id = id).all()
    return render_template("bookings/customer_bookings.jinja", bookings=bookings)

@booking_blueprint.route('/bookings/new')
def new_booking_form():
    treatments = Treatment.query.all()
    customers = Customer.query.all()
    rooms = Room.query.all()
    return render_template('bookings/new.jinja', title='make a booking', treatments=treatments, customers=customers, rooms=rooms)

@booking_blueprint.route('/show/<id>')
def show_booking(id):
    booking = Booking.query.get(id)
    return render_template('bookings/show_booking.jinja', booking = booking)

@booking_blueprint.route('/bookings/<id>/delete', methods=['POST'])
def delete_booking(id):
    booking = Booking.query.get(id)
    db.session.delete(booking)
    db.session.commit()
    return redirect ('/bookings')

@booking_blueprint.route('/bookings/<id>/edit')
def show_edit_booking_form(id):
    booking = Booking.query.get(id)
    treatments = Treatment.query.all()
    customers = Customer.query.all()
    return render_template('bookings/edit_booking_form.jinja', booking=booking, treatments=treatments, customers=customers)

@booking_blueprint.route('/bookings/<id>/edit', methods=["POST"])
def edit_booking(id):
    booking = Booking.query.get(id)
    db.session.commit()
    return redirect ('/bookings', booking=booking)

# ROOMS

@booking_blueprint.route('/rooms')
def rooms_index():
    rooms=Room.query.all()
    return render_template ('rooms/rooms_index.jinja', rooms=rooms)

@booking_blueprint.route('/rooms/<id>')
def show_room(id):
    bookings=Booking.query.filter_by(room_id=id).all()
    room = Room.query.get(id)
    return render_template('rooms/room_bookings.jinja', bookings=bookings, room=room)

