from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = None
SessionLocal = None
Base = declarative_base()


def init_db(url: str):
    global engine, SessionLocal
    engine = create_engine(url, echo=False)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return engine
