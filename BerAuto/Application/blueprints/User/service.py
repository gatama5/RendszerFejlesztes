

from sqlalchemy import select
from sqlalchemy.sql.functions import user
from Application import db
from Application.blueprints.User.shemas import UserResponseSchema
from Application.models.User import User
from Application.models.Car import Car
from Application.blueprints.User.shemas import CarResponseSchema



class UserService:

    @staticmethod
    def user_registrate(request):
        try:
            if db.session.execute(
                    select(User).filter_by(email = request["email"])
                ).scalar_one_or_none():
                return False, "Email already registered"
            user = User(**request)
            user.set_password(user.password)
            db.session.add(user)
            db.session.commit()
            return True, UserResponseSchema().dump(user)
        except Exception as ex:
            return False, "Incorrect user data!"

    @staticmethod
    def user_login(request):
        try:
            user = db.session.execute(
                select(User).filter_by(email=request["email"])
            ).scalar_one_or_none()
            if not user:
                return False, "Incorrect email!"
            if not user.check_password(request["password"]):
                return False, "Incorrect password!"
            return True, UserResponseSchema().dump(user)
        except Exception as ex:
            return False, "Incorrect user data!"

    @staticmethod
    def get_all_cars():
        try:
            cars = db.session.execute(select(Car)).scalars().all()
            return True, [CarResponseSchema().dump(car) for car in cars]
        except Exception as ex:
            return False, "Error fetching cars data!"

    @staticmethod
    def get_available_cars():
        try:
            available_cars = db.session.execute(
                select(Car).filter_by(available=True)
            ).scalars().all()
            return True, [CarResponseSchema().dump(car) for car in available_cars]
        except Exception as ex:
            return False, "Error fetching available cars data!"