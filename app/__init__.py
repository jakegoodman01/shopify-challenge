from flask import Flask

from app.db import init_db
from app.models.folder import FolderModel
from app.routes.delete import delete
from app.routes.get import get
from app.routes.upload import upload


def load_config(app, test_config):
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    load_config(app, test_config)

    # Initialize the database
    with app.app_context():
        init_db()

    # Register blueprints
    app.register_blueprint(upload)
    app.register_blueprint(get)
    app.register_blueprint(delete)

    return app




