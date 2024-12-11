from services.booking.api_booking import RestfulBookerAPI


class BaseTest:

    def setup_method(self):
        self.api_booking = RestfulBookerAPI()
