#!/usr/bin/python3
"""Definition of City class"""
from model_state import Base
from sqlalchemy import Column, Integer


class City(Base):
    """Representation of the City table 
    in the corresponding mysql db with 
    Attributes:
        id: id of the city
        name: name of the city
        state_id: the state id where the city is in
    """
    __tablename__ = 'cities'
    id = Column(Integer,
                unique=True,
                nullable=False,
                autoincrement=True,
                primary_key=True)
    name = Column(String(128),
                  nullable=False)
    state_id = Column(Integer,
                      nullable=False,
                      ForeignKey("states.id"))
