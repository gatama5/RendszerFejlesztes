from apiflask import APIBlueprint

bp = APIBlueprint('main', __name__, tag="User")

from Application.blueprints.User import routes