from sqlalchemy import create_engine

from models import BASE
from config import DATABASE_URL

if __name__ == "__main__":
    engine = create_engine(DATABASE_URL)
    BASE.metadata.create_all(engine)
