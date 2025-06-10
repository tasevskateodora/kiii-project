from pydantic import BaseModel


class ReservationSchema(BaseModel):
    reservation_id: str
    property_name: str
    host_name: str
    guest_name: str
    check_in_date: str
    price_per_night: float

