from faker import Faker
import requests
from dotenv import set_key, load_dotenv
import os

fake = Faker()

HOST = "https://restful-booker.herokuapp.com/"

payload_1 = {
    "username": "admin",
    "password": "password123"
}
#
# response = requests.post(
#     url=f"{HOST}/auth"
# )

# response = requests.get(
#     url=f"{HOST}/booking"
# )

response = requests.post(
        url=f"{HOST}/auth",
        headers={"Content-Type": f"application/json"},
        json=payload_1
    )
assert response.status_code == 200, response.json()
token = response.json().get("token")
set_key(".env", "SESSION_TOKEN", token)
assert token, "Ответ не содержит токен"
print(response.json())

payload_2 = {
    "firstname": fake.name(),
    "lastname": fake.last_name(),
    "totalprice": fake.random_int(),
    "depositpaid": fake.boolean(),
    "bookingdates": {
        "checkin": fake.date(),
        "checkout": fake.date()
        },
    "additionalneeds": fake.color_name()
}

response = requests.post(
        url=f"{HOST}/booking",
        headers={"Content-Type": f"application/json"},
        json=payload_2
    )
assert response.status_code == 200, response.json()
booking_id = response.json().get("bookingid")
set_key(".env", "BOOKING_ID", str(booking_id))
assert booking_id, "Ответ не содержит booking_id"
print(response.json())

payload_3 = {
    "firstname": "Jamess",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"
}

load_dotenv()

response = requests.put(
        url=f"{HOST}/booking/{os.getenv('BOOKING_ID')}",
        headers={
            "Content-Type": f"application/json",
            "Cookie": f"token={os.getenv('SESSION_TOKEN')}",

        },
        json=payload_3
    )
assert response.status_code == 200, response.json()

print(response.json())