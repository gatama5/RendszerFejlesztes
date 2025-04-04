from apiflask import APIBlueprint

bp = APIBlueprint('main', __name__, tag="main")

from Application.main import routes
