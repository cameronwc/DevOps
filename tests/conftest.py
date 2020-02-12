import pytest

from flask_app import create_app

@pytest.fixture
def client():
    flask_app = create_app()
    flask_app.debug = True
    return flask_app.test_client()
