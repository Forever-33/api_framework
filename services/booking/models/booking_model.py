from pydantic import BaseModel, field_validator, RootModel


class BaseValidator(BaseModel):
    @field_validator("*")
    def fields_are_not_empty(cls, value, field):
        if value == "" or value is None:
            raise ValueError(f"Поле {field.name} пустое")
        return value


class BookingDatesModel(BaseModel):
    checkin: str
    checkout: str


class BookingModel(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDatesModel
    additionalneeds: str


class BookingIdModel(BaseModel):
    bookingid: int
    booking: BookingModel


class BookingIds(BaseModel):
    bookingid: int


class BookingIdsList(BaseModel):
    object: list[BookingIds]


