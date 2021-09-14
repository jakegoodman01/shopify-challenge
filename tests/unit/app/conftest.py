import os
import tempfile

import pytest

from app import create_app
from app.db import init_db

from app.models.folder import FolderModel
from app.models.image import ImageModel


import pytest


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create a temporary file to isolate the database for each test
    db_fd, db_path = tempfile.mkstemp()
    # create the app with common test config
    app = create_app({"TESTING": True, "DATABASE": db_path})

    # create the database and load test data
    with app.app_context():
        init_db()

    yield app

    # close and remove the temporary database
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({'TESTING': True, 'DATABASE': db_path})

    with app.test_client() as client:
        with app.app_context():
            init_db()
        yield client

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


@pytest.fixture
def default_folder_model():
    return FolderModel('default-folder')


@pytest.fixture
def default_image_model():
    return ImageModel('default-folder/default_image.jpg')
