from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base, UserMixin):

    """Data model example."""
    __tablename__ = "Users"
    __table_args__ = {"schema": "example"}

    id = Column(Integer, primary_key = True)
    username = Column(String(100), unique=True)
    password = Column(String(100))
    name = Column(String(500))
