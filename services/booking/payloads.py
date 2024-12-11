from faker import Faker

fake = Faker()


class Payloads:
    create_booking = {
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

    update_booking = {
        "firstname": fake.name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(),
        "depositpaid": fake.boolean(),
        "bookingdates": {
            "checkin": fake.date(),
            "checkout": fake.date()
        },
        "additionalneeds": fake.last_name()
    }

    patch_update_booking = {
        "firstname": fake.name(),
        "lastname": fake.last_name(),
    }

    empty_json = {

    }
