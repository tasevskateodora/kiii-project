import time

from fastapi import Depends, FastAPI
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from app.crud import create, delete, list_all, read, update
from app.db import SessionLocal, engine
from app.models import Base
from app.schemas import ReservationSchema

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend адреса
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
for i in range(5):
    try:
        Base.metadata.create_all(bind=engine)
        break
    except OperationalError:
        time.sleep(i + 1)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.post("/create")
async def create_reservation(schema: ReservationSchema, db: Session = Depends(get_db)):
    reservation = create(db, schema)

    if reservation is None:
        return {"message": "Reservation already exists"}
    else:
        return reservation


@app.get("/read/{reservation_id}")
async def read_reservation(reservation_id: str, db: Session = Depends(get_db)):
    reservation = read(db, reservation_id)

    if reservation is None:
        return {"message": "Reservation not found"}
    else:
        return reservation


@app.post("/update")
async def update_reservation(schema: ReservationSchema, db: Session = Depends(get_db)):
    reservation = update(db, schema)

    if reservation is None:
        return {"message": "Reservation not found"}
    else:
        return reservation


@app.post("/delete/{reservation_id}")
async def delete_reservation(reservation_id: str, db: Session = Depends(get_db)):
    reservation = delete(db, reservation_id)

    if reservation is None:
        return {"message": "Reservation not found"}
    else:
        return reservation


@app.get("/list")
async def list_all_reservations(db: Session = Depends(get_db)):
    return list_all(db)
