from flask import Flask
from config import config_by_name
from .database import db


def create_app(config_name: str) -> Flask:
    """
        Creates and configures an instance of the Flask application.
    """

    app = Flask(__name__)

    # Load the appropriate configuration.
    app.config.from_object(config_by_name[config_name])

    # Initialize the database with the application.
    db.init_app(app)

    # Record the Blueprints.
    from .api.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    @app.route('/health')
    def health_check():
        return 'OK', 200

    return app