from apiflask import APIBlueprint

bp = APIBlueprint('main', __name__, tag="main")

@bp.route("/")
def index():
    return "Hello World!"

from Application.blueprints.User import bp as user_bp
bp.register_blueprint(user_bp, url_prefix="/api")


from Application.main import routes
