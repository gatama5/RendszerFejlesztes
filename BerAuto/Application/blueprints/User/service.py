from Application import db
from Application.blueprints.User.shemas import UserResponseSchema
from Application.models.User import User

class UserService:

    @staticmethod
    def user_registrate(request):
        if db.session.execute(
            select(User).filter_by(email = request["email"])
        ).scalar_one_or_none():
            return False, "Email already registered"

    @staticmethod
    def user_login(request):
        pass