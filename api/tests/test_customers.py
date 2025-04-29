from fastapi.testclient import TestClient
from ..main import app
from ..controllers import customers
from ..models import customers as customer_models
import pytest
from datetime import datetime



client = TestClient(app)

@pytest.fixture
def db_session(mocker):
    return mocker.Mock()

def test_create_customer(db_session):
    customer_data = {
        "name": "Sander Wich",
        "email": "s.wich@hungry.com",
        "phone": "1238675309",
        "address": "123 Address St."
    }
    customer = customer_models.Customers(**customer_data)
    created_customer = customers.create(db_session, customer)

    assert created_customer is not None
    assert created_customer.name == "Sander Wich"
    assert created_customer.email == "s.wich@hungry.com"
    assert created_customer.phone == "1238675309"
    assert created_customer.address == "123 Address St."