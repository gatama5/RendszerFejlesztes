from apiflask import APIBlueprint

bp = APIBlueprint('main', __name__, tag="Admin")

from Application.blueprints.User import routes