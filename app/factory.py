from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    app.secret_key = '123456'

    from app.blueprints import main
    app.register_blueprint(main.bp)

    return app