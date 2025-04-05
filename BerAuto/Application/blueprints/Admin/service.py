
from sqlalchemy import select
from Application import db
from Application.models import Car
from Application.models.Admin import Admin
from Application.blueprints.Admin.shemas import AdminResponseSchema, CarDetailSchema


class AdminService:
    @staticmethod
    def admin_login(request):
        try:
            admin = db.session.execute(
                select(Admin).filter_by(email=request["email"])
            ).scalar_one_or_none()

            if not admin:
                return False, "Incorrect email or user is not an admin!"

            if not admin.check_password(request["password"]):
                return False, "Incorrect password!"

            return True, AdminResponseSchema().dump(admin)
        except Exception as ex:
            return False, f"Login failed: {str(ex)}"

    @staticmethod
    def get_cars_data():
        try:
            cars = db.session.execute(select(Car)).scalars().all()
            return True, [CarDetailSchema().dump(car) for car in cars]
        except Exception as ex:
            return False, f"Error fetching cars data: {str(ex)}"

    @staticmethod
    def delete_car(request):
        try:
            car = db.session.execute(
                select(Car).filter_by(id=request["car_id"])
            ).scalar_one_or_none()

            if not car:
                return False, "Car not found"

            if not car.available:
                return False, "Cannot delete car that is currently unavailable (might be in use)"

            db.session.delete(car)
            db.session.commit()

            return True, {"message": f"Car with ID {car.id} successfully deleted"}
        except Exception as ex:
            db.session.rollback()
            return False, f"Error deleting car: {str(ex)}"

    @staticmethod
    def update_car(request):
        try:
            car = db.session.execute(
                select(Car).filter_by(id=request["id"])
            ).scalar_one_or_none()

            if not car:
                return False, "Car not found"

            for key, value in request.items():
                if key != 'id' and value is not None:
                    setattr(car, key, value)

            db.session.commit()

            return True, {
                "message": f"Car with ID {car.id} successfully updated",
                "car": {
                    "id": car.id,
                    "licensePlate": car.licensePlate,
                    "brand": car.brand,
                    "model": car.model,
                    "year": car.year,
                    "fuelType": car.fuelType,
                    "km": car.km,
                    "state": car.state,
                    "available": car.available
                }
            }
        except Exception as ex:
            db.session.rollback()
            return False, f"Error updating car: {str(ex)}"

    @staticmethod
    def create_car(request):
        try:
            # Ellenőrzés, hogy létezik-e már ilyen rendszámú autó
            existing_car = db.session.execute(
                select(Car).filter_by(licensePlate=request["licensePlate"])
            ).scalar_one_or_none()

            if existing_car:
                return False, "Car with this license plate already exists"

            # Új autó létrehozása a modellben definiált attribútumok szerint
            new_car = Car()
            new_car.licensePlate = request["licensePlate"]
            new_car.brand = request["brand"]
            new_car.model = request["model"]
            new_car.year = request["year"]
            new_car.fuelType = request["fuelType"]
            new_car.km = request["km"]
            new_car.state = request["state"]
            new_car.available = request.get("available", True)

            db.session.add(new_car)
            db.session.commit()

            return True, {
                "message": "Car successfully created",
                "car": {
                    "id": new_car.id,
                    "licensePlate": new_car.licensePlate,
                    "brand": new_car.brand,
                    "model": new_car.model,
                    "year": new_car.year,
                    "fuelType": new_car.fuelType,
                    "km": new_car.km,
                    "state": new_car.state,
                    "available": new_car.available
                }
            }
        except Exception as ex:
            db.session.rollback()
            return False, f"Error creating car: {str(ex)}"

    @staticmethod
    def update_car_km(request):
        try:
            car = db.session.execute(
                select(Car).filter_by(id=request["car_id"])
            ).scalar_one_or_none()

            if not car:
                return False, "Car not found"

            if request["km"] < car.km:
                return False, "New odometer value cannot be less than the current value"

            car.km = request["km"]
            db.session.commit()

            return True, {
                "message": f"Car odometer successfully updated",
                "car": {
                    "id": car.id,
                    "licensePlate": car.licensePlate,
                    "km": car.km
                }
            }
        except Exception as ex:
            db.session.rollback()
            return False, f"Error updating odometer: {str(ex)}"