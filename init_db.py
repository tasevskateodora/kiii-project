from app.db import engine
from app.models import Base

Base.metadata.create_all(bind=engine)
print("Tables created!")
