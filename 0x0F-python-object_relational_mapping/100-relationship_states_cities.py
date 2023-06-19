#!/usr/bin/python3
"""Creates the State "California" with City "San Francisco" from db"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(engine)
    session = Session()
    session.add(City(name="San Francisco", state_id=1))
    session.commit()
