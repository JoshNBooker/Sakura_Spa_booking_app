from flask import Flask, render_template, redirect, Blueprint, request
from app import db
from models import Customer, Treatment, Booking,Room
from datetime import datetime, timedelta
from controller.booking_controller import check_booking
