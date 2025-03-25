from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate
from flask_login import LoginManager

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "qwedasdqweasdqweasd"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    migrate = Migrate(app, db)

    # Modellek importálása
    from Application.User import User
    from Application.Customer import Customer
    from Application.Owner import Owner
    from Application.CarManager import CarManager

    # Útvonalak regisztrálása
    from Application.routes import register_routes
    register_routes(app)

    return app