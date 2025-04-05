from Application.blueprints.User import bp
from Application.blueprints.User.service import UserService
from Application.blueprints.User.shemas import UserRequestSchema, UserResponseSchema, UserLoginSchema
from apiflask import HTTPError

@bp.route("/user")
def user():
    return "Hello user!"

@bp.post("/registrate")
@bp.input(UserRequestSchema,location="json")
@bp.output(UserResponseSchema)
def user_registrate(json_data):
    success, response = UserService.user_registrate(json_data)
    if success:
        return response, 201
    raise HTTPError(message=response, status_code=400)

@bp.post("/login")
@bp.input(UserLoginSchema,location="json")
@bp.output(UserResponseSchema)
def user_login(json_data):
    success, response = UserService.user_login(json_data)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)