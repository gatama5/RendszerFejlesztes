from apiflask import APIFlask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate
from flask_login import LoginManager

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
login_manager = LoginManager()

def create_app():
    app = APIFlask(__name__, json_errors=True,
                   docs_path="/swagger",title="Berauto API")
    app.config["SECRET_KEY"] = "qwedasdqweasdqweasd"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    migrate = Migrate(app, db)

    # Modellek importálása
    from Application.models.User import User
    from Application.models.Customer import Customer
    from Application.models.Owner import Owner
    from Application.models.CarManager import CarManager

    # Útvonalak regisztrálása
    # from Application.main import register_routes
    # register_routes(app)

    # Register Blueprints
    from Application.blueprints import bp as main_bp
    app.register_blueprint(main_bp, url_prefix="/api")

    return app