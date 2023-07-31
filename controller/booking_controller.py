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
    room_id = request.form["room"]
    new_booking = Booking(date_time = date_time,customer_id = customer_id,treatment_id = treatment_id, room_id = room_id)
    is_available = True
    for b in Booking.query.all():
        new_date_time = datetime.strptime((date_time[0:10] + " " + date_time[11:16]), "%Y-%m-%d %H:%M")
        two_hours = timedelta(hours=2)
        booking_start = b.date_time - two_hours
        booking_end = b.date_time + two_hours
        booking_room_id = b.room_id
        if new_date_time >= booking_start and new_date_time <= booking_end and int(room_id) == booking_room_id:
            is_available = False
    if is_available:
        db.session.add(new_booking)
        db.session.commit()
        return redirect("/bookings/success")
    else:
        return redirect('/bookings/denied')
        
@booking_blueprint.route('/bookings/success')
def new_booking_success():
    bookings = Booking.query.all()
    customers = Customer.query.all()
    treatments = Treatment.query.all()
    rooms = Room.query.all()
    return render_template('bookings/success.jinja', bookings=bookings, customers=customers, treatments=treatments, rooms=rooms)

@booking_blueprint.route('/bookings/denied')
def new_booking_failure():
    bookings = Booking.query.all()
    customers = Customer.query.all()
    treatments = Treatment.query.all()
    rooms = Room.query.all()
    return render_template('bookings/denied.jinja',bookings=bookings, customers=customers, treatments=treatments, rooms=rooms)

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

