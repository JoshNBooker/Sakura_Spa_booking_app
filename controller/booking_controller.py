from flask import Flask, render_template, redirect, Blueprint, request
from app import db
from models import Customer, Treatment, Booking

booking_blueprint = Blueprint('booking',__name__)

@booking_blueprint.route('/')
def home_page():
    return render_template('index.jinja', title = 'Sakura Spa')

@booking_blueprint.route('/bookings')
def display_bookings():
    return render_template('bookings/diary.jinja', title = 'Diary')

@booking_blueprint.route('/bookings/new')
def new_booking_form():
    treatments = Treatment.query.all()
    customers = Customer.query.all()
    return render_template('bookings/new.jinja', title='make a booking', treatments=treatments, customers=customers)
