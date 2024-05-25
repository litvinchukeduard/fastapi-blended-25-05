from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2://postgres:admin@localhost/recipes")

Session = sessionmaker(engine)


def get_db_connection():
    db = Session()
    try:
        yield db
    finally:
        db.close()
