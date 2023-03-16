#!/usr/bin/python3
"""city model"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import State

base = declarative_base()


class City(base):
    """city class"""

    __tablename__ = "cities"

    id = Column("id", autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column("name", String(128), nullable=False)

    state_id = Column("state_id", Integer, ForeignKey(
        State.id), nullable=False)
