from os import environ
from Application import create_app, db

app = create_app()

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '8080'))
    except ValueError:
        PORT = 8080

    with app.app_context():
        db.create_all()

    app.run(host=HOST, port=PORT, debug=True)