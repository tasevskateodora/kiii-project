from sqlalchemy.orm import Session
from . import models
from . import schemas


def create(db: Session, schema: schemas.ReservationSchema):
    """
    Create a reservation.

    Args:
        db (Session): The database session object.
        schema (ReservationSchema): The reservation schema.

    Returns:
        Reservation | None: The created reservation, unless one with the same reservation_id already exists.
    """

    existing_reservation = read(db, schema.reservation_id)

    if existing_reservation is not None:
        return None

    reservation = models.Reservation(
        reservation_id=schema.reservation_id,
        property_name=schema.property_name,
        host_name=schema.host_name,
        guest_name=schema.guest_name,
        check_in_date=schema.check_in_date,
        price_per_night=schema.price_per_night,
    )
    db.add(reservation)
    db.commit()
    db.refresh(reservation)

    return reservation


def read(db: Session, reservation_id: str):
    """
    Read a reservation.

    Args:
        db (Session): The database session object.
        reservation_id (str): The reservation ID.

    Returns:
        Reservation | None: The reservation, if it exists.
    """

    return db.query(models.Reservation).filter(models.Reservation.reservation_id == reservation_id).first()


def update(db: Session, schema: schemas.ReservationSchema):
    """
    Update a reservation.

    Args:
        db (Session): The database session object.
        schema (ReservationSchema): The reservation schema.

    Returns:
        Reservation | None: The reservation, if it exists.
    """

    reservation = read(db, schema.reservation_id)

    if reservation is None:
        return None

    reservation.property_name = schema.property_name
    reservation.host_name = schema.host_name
    reservation.guest_name = schema.guest_name
    reservation.check_in_date = schema.check_in_date
    reservation.price_per_night = schema.price_per_night

    db.commit()
    db.refresh(reservation)

    return reservation


def delete(db: Session, reservation_id: str):
    """
    Delete a reservation.

    Args:
        db (Session): The database session object.
        reservation_id (str): The reservation ID.

    Returns:
        Reservation | None: The reservation, if it exists.
    """

    reservation = read(db, reservation_id)

    if reservation is None:
        return None

    db.delete(reservation)
    db.commit()

    return reservation


def list_all(db: Session):
    """
    Get all reservations.

    Args:
        db (Session): The database session object.

    Returns:
        list[Reservation]: The list of all reservations.
    """

    return db.query(models.Reservation).all()
