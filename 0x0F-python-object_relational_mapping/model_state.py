#!/usr/bin/python3
"""Definition of a State class"""
from sqlalchemy import Integer,String,Column, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

class State(Base):
    """Class with id and name attriutes of each state"""
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, 
                unique=True,
                primary_key=True,
                nullable=False)
    name = Column(String(128),
                  nullable=False)
