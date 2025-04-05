from marshmallow import Schema, fields
from apiflask.validators import Email

class UserRequestSchema(Schema):
    username = fields.String(required=True)
    name = fields.String(required=True)
    email = fields.String(validate=Email(), required=True)
    phone = fields.String(required=True)
    address = fields.String(required=True)
    password = fields.String(required=True)

class UserResponseSchema(Schema):
    id = fields.Integer()
    username = fields.String(required=True)
    name = fields.String(required=True)
    email = fields.String(validate=Email(), required=True)
    phone = fields.String(required=True)
    address = fields.String(required=True)

class UserLoginSchema(Schema):
    email = fields.String(validate = Email(), required=True)
    password = fields.String(required=True)

class CarResponseSchema(Schema):
    id = fields.Integer()
    licensePlate = fields.String()
    brand = fields.String()
    model = fields.String()
    year = fields.Integer()
    fuelType = fields.String()
    km = fields.Integer()
    state = fields.String()
    available = fields.Boolean()