import allure
import requests
from dotenv import set_key

from utils.helper import Helper
from services.booking.endpoints import Endpoints
from services.booking.payloads import Payloads
from config.headers import Headers
from services.booking.models.booking_model import BookingIdModel, BookingModel, BookingIdsList


class RestfulBookerAPI(Helper):
    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Создание - Create Booking")
    def create_booking(self):
        response = requests.post(
            url=self.endpoints.create_booking,
            headers=self.headers.basic,
            json=self.payloads.create_booking
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        booking_id = response.json().get("bookingid")
        set_key(".env", "BOOKING_ID", str(booking_id))
        model = BookingIdModel(**response.json())
        print(model)
        return model

    @allure.step("Получение одного booking id - Get Booking by id")
    def get_bookings_id(self):
        response = requests.get(
            url=self.endpoints.get_booking_by_id,
            headers=self.headers.basic
        )
        assert response.status_code == 200, response.json()
        print(self.attach_response(response.json()))
        model = BookingModel(**response.json())
        print(model)
        return model

    @allure.step("Обновление - Update booking by ID")
    def update_booking(self):
        response = requests.put(
            url=self.endpoints.update_booking_by_id,
            headers=self.headers.update,
            json=self.payloads.update_booking,
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = BookingModel(**response.json())
        print(model)
        return model

    @allure.step("Получение списка bookingid's - Get Booking by ids")
    def get_bookings_ids(self):
        response = requests.get(
            url=self.endpoints.get_booking_by_ids,
        )
        assert response.status_code == 200, response.json()
        print(self.attach_response(response.json()))
        model = BookingIdsList(object=response.json())
        print(model)
        return model

    @allure.step("Обновление частичное - Patch Update booking by ID")
    def partial_update_booking(self):
        response = requests.patch(
            url=self.endpoints.partial_update_booking,
            headers=self.headers.update,
            json=self.payloads.patch_update_booking,
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = BookingModel(**response.json())
        print(model)
        return model

    @allure.step("Удаление booking - Delete booking by ID")
    def delete_booking(self):
        response = requests.delete(
            url=self.endpoints.delete_booking,
            headers=self.headers.delete,
        )
        assert response.status_code == 201, response.json()

    @allure.step("Создание booking с пустым json - Create Booking")
    def create_booking_empty_json(self):
        response = requests.post(
            url=self.endpoints.create_booking,
            headers=self.headers.basic,
            json=self.payloads.empty_json
        )
        assert response.status_code == 500

    @allure.step("Получение пустого booking id - Get Booking by empty id")
    def get_empty_bookings_id(self):
        response = requests.get(
            url=self.endpoints.empty_booking_id,
            headers=self.headers.basic
        )
        assert response.status_code == 404

    @allure.step("Обновление c пустым json - Update booking by ID")
    def update_empty_booking(self):
        response = requests.put(
            url=self.endpoints.update_booking_by_id,
            headers=self.headers.update,
            json=self.payloads.empty_json,
        )
        assert response.status_code == 400

    @allure.step("Обновление c пустым json - Update booking by ID")
    def update_empty_id_booking(self):
        response = requests.put(
            url=self.endpoints.empty_booking_id,
            headers=self.headers.update,
            json=self.payloads.update_booking,
        )
        assert response.status_code == 405

    @allure.step("Частичное обновление c пустым json - Patch Update booking by ID")
    def partial_update_booking_empty_json(self):
        response = requests.patch(
            url=self.endpoints.partial_update_booking,
            headers=self.headers.update,
            json=self.payloads.empty_json,
        )
        assert response.status_code == 405

    @allure.step("Отправка запроса c пустыми заголовками - Patch Update booking by ID")
    def partial_update_empty_headers(self):
        response = requests.patch(
            url=self.endpoints.partial_update_booking,
            headers=self.headers.empty_headers,
            json=self.payloads.empty_json,
        )
        assert response.status_code == 403
