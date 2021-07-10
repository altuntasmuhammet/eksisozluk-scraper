from sqlalchemy import create_engine, Column
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String, DateTime)
from scrapy.utils.project import get_project_settings
from django.conf import settings

Base = declarative_base()


def db_connect() -> Engine:
    """
    Creates database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    DATABASE = {
        "drivername": "postgresql",
        "host": settings.POSTGRES_HOST,
        "port": settings.POSTGRES_PORT,
        "username": settings.POSTGRES_USER,
        "password": settings.POSTGRES_PASSWORD,
        "database": settings.POSTGRES_DB,
    }
    return create_engine(URL(**DATABASE))


def create_entries_table(engine: Engine):
    """
    Create the Items table
    """
    Base.metadata.create_all(engine)


class Entry(Base):
    __tablename__ = 'entries'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    favourite_count = Column(Integer)
    author = Column(String)
    created_date = Column(DateTime)
    edited_date = Column(DateTime, nullable=True)
    eksisozluk_entry_id = Column(Integer, unique=True)
    eksisozluk_author_id = Column(Integer)
