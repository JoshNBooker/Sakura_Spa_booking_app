from flask import Flask, render_template, redirect, Blueprint, request
from app import db
from models import Customer, Treatment, Booking,Room
from datetime import datetime, timedelta


d1 = datetime(2023,7,11, 12,50,00)
d2 = datetime(2023,7,13, 13,00,00)

if d1 > d2 + datetime():
    print(yes)

print(Booking.query.all(room_id))

