from flask import Flask, render_template, redirect, Blueprint, request
from app import db
from models import Customer, Treatment, Booking

booking_blueprint = Blueprint('booking',__name__)

@booking_blueprint.route('/')
def home_page():
    return render_template('index.jinja', title = 'Sakura Spa')

@booking_blueprint.route('/bookings')
def display_bookings():
    bookings = Booking.query.all()
    customers = Customer.query.all()
    return render_template('bookings/diary.jinja', title = 'Diary', bookings=bookings, customers=customers)

@booking_blueprint.route('/bookings', methods=["POST"])
def submit_new_booking():
    date_time = request.form["date_time"]
    customer_id = request.form["customer"]
    treatment_id = request.form["treatment"]
    new_booking = Booking(date_time = date_time,customer_id = customer_id,treatment_id = treatment_id)
    db.session.add(new_booking)
    db.session.commit()
    return redirect('/bookings')

@booking_blueprint.route('/bookings/<id>')
def show_customers_bookings(id):
    bookings = Booking.query.filter_by(customer_id = id).all()
    return render_template('bookings/customer_bookings.jinja', bookings=bookings)


@booking_blueprint.route('/bookings/new')
def new_booking_form():
    treatments = Treatment.query.all()
    customers = Customer.query.all()
    return render_template('bookings/new.jinja', title='make a booking', treatments=treatments, customers=customers)

@booking_blueprint.route('/show/<id>')
def show_booking(id):
    booking = Booking.query.get(id)
    return render_template('bookings/show_booking.jinja', booking = booking)

