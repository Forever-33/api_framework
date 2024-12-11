import os

import requests
import pytest
from dotenv import set_key, load_dotenv

load_dotenv()

HOST = "https://restful-booker.herokuapp.com/"

payload_init_environment = {
         "username": "admin",
         "password": "password123"
    }


@pytest.fixture(autouse=True, scope='session')
def init_environment():
    response = requests.post(
        url=f"{HOST}/auth",
        headers={"Content-Type": f"application/json"},
        json=payload_init_environment
    )
    assert response.status_code == 200, response.json()
    token = response.json().get("token")
    set_key(".env", "SESSION_TOKEN", token)
    return token


payload_id_booking = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }


@pytest.fixture(autouse=True, scope='session')
def id_booking():
    response = requests.post(
        url=f"{HOST}/booking",
        headers={"Content-Type": f"application/json"},
        json=payload_id_booking
    )
    assert response.status_code == 200, response.json()
    booking_id = response.json().get("bookingid")
    set_key(".env", "BOOKING_ID", str(booking_id))
    return booking_id


