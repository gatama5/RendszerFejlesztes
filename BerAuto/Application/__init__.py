from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SECRET_KEY"] = "qwedasdqweasdqweasd"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"

db.init_app(app)

migrate = Migrate(app, db)

from Application.User import User
from Application.Customer import Customer
from Application.Owner import Owner
from Application.CarManager import CarManager

from Application import routes