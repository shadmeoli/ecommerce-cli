import os
import datetime

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, DateTime

load_dotenv()


engine = create_engine("sqlite///ecomerce.sqlite", echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)


class Auth:

    def __init__(self) -> None:
        pass

    def signup(self, username: str, email: str, password: str):
        pass
