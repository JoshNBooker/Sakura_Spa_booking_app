from app import db
from models import Customer,Booking,Treatment, Room
import click

from flask.cli import with_appcontext

@click.command(name='seed')
@with_appcontext
def seed():
    Booking.query.delete()
    Customer.query.delete()
    Treatment.query.delete()
    Room.query.delete()
    
    customer1 = Customer(first_name="Bilbo", last_name="Baggins")
    customer2 = Customer(first_name="Mike", last_name="Ehrmantraut")
    customer3 = Customer(first_name="Jeff", last_name = "Goldblum")

    db.session.add(customer1)
    db.session.add(customer2)
    db.session.add(customer3)

    treatment1 = Treatment(name="massage")
    treatment2 = Treatment(name="sauna")
    treatment3 = Treatment(name="hot stone therapy")
    treatment4 = Treatment(name="cold plunge")
    treatment5 = Treatment(name="facial massage")
    treatment6 = Treatment(name="nutrition class")

    db.session.add(treatment1)
    db.session.add(treatment2)
    db.session.add(treatment3)
    db.session.add(treatment4)
    db.session.add(treatment5)
    db.session.add(treatment6)
    db.session.commit()

    room1 = Room(name="Massage Room 1")
    room2 = Room(name="Massage Room 2")
    room3 = Room(name="Sauna 1")
    room4 = Room(name="Sauna 2")
    room5 = Room(name="Hot Stone Therapy Room")
    room6 = Room(name="Cold Plunge Tank")
    room7 = Room(name="Kitchen")

    db.session.add(room1)
    db.session.add(room2)
    db.session.add(room3)
    db.session.add(room4)
    db.session.add(room5)
    db.session.add(room6)
    db.session.add(room7)
    db.session.commit()


    booking1 = Booking(date_time="2023-07-11 12:50", customer_id=customer1.id, treatment_id=treatment1.id, room_id=room1.id) 
    booking2 = Booking(date_time="2023-07-13 13:00", customer_id=customer2.id, treatment_id=treatment2.id, room_id=room3.id)
    booking3 = Booking(date_time="2023-07-14 13:45", customer_id=customer3.id, treatment_id=treatment3.id, room_id=room5.id)
    booking4 = Booking(date_time="2023-07-14 14:00", customer_id=customer2.id, treatment_id=treatment4.id, room_id=room6.id)
    booking5 = Booking(date_time="2023-07-15 12:00", customer_id=customer1.id, treatment_id=treatment5.id, room_id=room5.id)


    db.session.add(booking1)
    db.session.add(booking2)
    db.session.add(booking3)
    db.session.add(booking4)
    db.session.add(booking5)

    db.session.commit()