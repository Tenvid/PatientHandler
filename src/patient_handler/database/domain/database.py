from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import declarative_base, sessionmaker


BASE = declarative_base()
engine = create_engine("sqlite+pysqlite:///./patients.db")
SessionLocal = sessionmaker(bind=engine)


def get_engine() -> Engine:
    return create_engine("sqlite+pysqlite:///./patients.db")


def load_all(engine: Engine):
    BASE.metadata.create_all(engine)
