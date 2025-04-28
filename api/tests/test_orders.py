from fastapi.testclient import TestClient
from ..controllers import orders
from ..main import app
import pytest
from ..models import orders as order_models
from datetime import datetime

client = TestClient(app)

@pytest.fixture
def db_session(mocker):
    return mocker.Mock()

def test_create_order(db_session):
    order_data = {
        "customer_id": 1,
        "description": "Test order",
        "order_date": datetime.utcnow(),
        "tracking_number": 123456,
        "status": "pending"
    }

    order_object = order_models.Order(**order_data)

    created_order = orders.create(db_session, order_object)

    assert created_order is not None
    assert created_order.customer_id == 1
    assert created_order.description == "Test order"
    assert created_order.tracking_number == 123456
    assert created_order.status == "pending"
