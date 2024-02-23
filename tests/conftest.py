from app import app
import pytest
# import os
from dotenv import load_dotenv
# from flask_migrate import upgrade, downgrade

load_dotenv()

@pytest.fixture
def test_app():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
    with app.app_context():
        yield app