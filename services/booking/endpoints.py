import os

from dotenv import load_dotenv

HOST = "https://restful-booker.herokuapp.com/"

load_dotenv()


class Endpoints:

    create_booking = f"{HOST}/booking"
    update_booking_by_id = f"{HOST}/booking/{os.getenv('BOOKING_ID')}"
    get_booking_by_ids = f"{HOST}/booking"
    get_booking_by_id = f"{HOST}/booking/{os.getenv('BOOKING_ID')}"
    partial_update_booking = f"{HOST}/booking/{os.getenv('BOOKING_ID')}"
    delete_booking = f"{HOST}/booking/{os.getenv('BOOKING_ID')}"
    empty_booking_id = f"{HOST}/booking/ "

