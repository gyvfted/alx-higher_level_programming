#!/usr/bin/python3
"""python file that contains the class and Base, an instance of declarative_base()"""

from enum import unique
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

Base = declarative_base()


class State(Base):
    """Class State"""

    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
