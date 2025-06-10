from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    ...


class Reservation(Base):
    __tablename__ = "reservations"

    reservation_id: Mapped[str] = mapped_column(primary_key=True)
    property_name: Mapped[str]
    host_name: Mapped[str]
    guest_name: Mapped[str]
    check_in_date: Mapped[str]
    price_per_night: Mapped[float]

    def __repr__(self) -> str:
        return f"{self.property_name!r} ({self.reservation_id!r})"

