import allure
import pytest

from config.base_test import BaseTest


@allure.epic('Administration')
@allure.feature('Booking')
class TestBooking(BaseTest):

    @pytest.mark.regression
    @allure.title("Create new booking")
    def test_create_booking(self):
        booking = self.api_booking.create_booking()

    @pytest.mark.regression
    @allure.title("Get bookingid")
    def test_get_booking_id(self):
        print(self.api_booking.get_bookings_id())

    @pytest.mark.regression
    @allure.title("Update booking")
    def test_update_booking(self):
        print(self.api_booking.update_booking())

    @pytest.mark.regression
    @allure.title("Get bookingid's")
    def test_get_booking_ids(self):
        print(self.api_booking.get_bookings_ids())

    @pytest.mark.regression
    @allure.title("Partial Update Booking")
    def test_patch_booking_ids(self):
        print(self.api_booking.partial_update_booking())

    @pytest.mark.regression
    @allure.title("Delete Booking")
    def test_delete_booking(self):
        print(self.api_booking.delete_booking())

    @allure.title("Create booking for empty json")
    def test_create_empty_json(self):
        print(self.api_booking.create_booking_empty_json())

    @allure.title("Get empty bookingid")
    def test_get_empty_id(self):
        print(self.api_booking.get_empty_bookings_id())

    @allure.title("Update booking empty json")
    def test_update_empty_booking(self):
        print(self.api_booking.update_empty_booking())

    @allure.title("Update booking empty id")
    def test_update_empty_id_booking(self):
        print(self.api_booking.update_empty_id_booking())

    @allure.title("Partial update booking empty json")
    def test_partial_update_empty_json_booking(self):
        print(self.api_booking.partial_update_booking_empty_json())

    @allure.title("Partial update booking empty headers")
    def test_partial_update_empty_header(self):
        print(self.api_booking.partial_update_empty_headers())
