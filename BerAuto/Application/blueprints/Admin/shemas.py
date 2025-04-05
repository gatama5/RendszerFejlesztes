from marshmallow import Schema, fields
from apiflask.validators import Email

class AdminLoginSchema(Schema):
    email = fields.String(validate=Email(), required=True)
    password = fields.String(required=True)

class AdminResponseSchema(Schema):
    id = fields.Integer()
    username = fields.String()
    name = fields.String()
    email = fields.String()
    phone = fields.String()
    address = fields.String()
    is_superadmin = fields.Boolean()

class CarDetailSchema(Schema):
    id = fields.Integer()
    licensePlate = fields.String()
    brand = fields.String()
    model = fields.String()
    year = fields.Integer()
    fuelType = fields.String()
    km = fields.Integer()
    state = fields.String()
    available = fields.Boolean()

class CarIdSchema(Schema):
    car_id = fields.Integer(required=True)

class CarUpdateSchema(Schema):
    id = fields.Integer(required=True)
    licensePlate = fields.String(required=False)
    brand = fields.String(required=False)
    model = fields.String(required=False)
    year = fields.Integer(required=False)
    fuelType = fields.String(required=False)
    km = fields.Integer(required=False)
    state = fields.String(required=False)
    available = fields.Boolean(required=False)

class CarCreateSchema(Schema):
    licensePlate = fields.String(required=True)
    brand = fields.String(required=True)
    model = fields.String(required=True)
    year = fields.Integer(required=True)
    fuelType = fields.String(required=True)
    km = fields.Integer(required=True)
    state = fields.String(required=True)
    available = fields.Boolean(required=False, default=True)

class CarUpdateKmSchema(Schema):
    car_id = fields.Integer(required=True)
    km = fields.Integer(required=True)