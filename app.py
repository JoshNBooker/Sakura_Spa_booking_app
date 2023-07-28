from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://josh@localhost:5432/booking_app"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from controller.booking_controller import booking_blueprint
from models import Customer, Booking, Treatment

app.register_blueprint(booking_blueprint)
from seed import seed
app.cli.add_command(seed)

