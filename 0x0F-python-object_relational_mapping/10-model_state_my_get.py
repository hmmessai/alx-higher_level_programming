#!/usr/bin/python3
"""Prints the State object with the name passed as argument from db"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(''
                           )
