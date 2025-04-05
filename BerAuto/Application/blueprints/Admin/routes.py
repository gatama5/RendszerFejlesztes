from Application.blueprints.Admin import bp
from Application.blueprints.Admin.service import AdminService
from Application.blueprints.Admin.shemas import AdminLoginSchema, AdminResponseSchema, CarDetailSchema, CarIdSchema, \
    CarUpdateSchema, CarCreateSchema, CarUpdateKmSchema
from apiflask import HTTPError

@bp.route("/admin")
def admin():
    return "Admin panel"

@bp.post("/login")
@bp.input(AdminLoginSchema, location="json")
@bp.output(AdminResponseSchema)
def admin_login(json_data):
    success, response = AdminService.admin_login(json_data)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=401)

@bp.route("/cars/details")
@bp.output(CarDetailSchema(many=True))
def get_cars_details():
    success, response = AdminService.get_cars_data()
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)

@bp.delete("/cars/delete")
@bp.input(CarIdSchema, location="json")
def delete_car(json_data):
    success, response = AdminService.delete_car(json_data)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)

@bp.put("/cars/update")
@bp.input(CarUpdateSchema, location="json")
def update_car(json_data):
    success, response = AdminService.update_car(json_data)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)

@bp.post("/cars/create")
@bp.input(CarCreateSchema, location="json")
def create_car(json_data):
    success, response = AdminService.create_car(json_data)
    if success:
        return response, 201
    raise HTTPError(message=response, status_code=400)

@bp.put("/cars/update-km")
@bp.input(CarUpdateKmSchema, location="json")
def update_car_km(json_data):
    success, response = AdminService.update_car_km(json_data)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)