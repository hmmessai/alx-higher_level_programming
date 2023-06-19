#!/usr/bin/python3
""" Lists all State objects and corresponding
    City objects contained in the db"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import relationship


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).order_by(State.id):
        print("{}: {}".format(instance.id, instance.name))
        for city_inst in instance.cities:
            print("    ", end="")
            print("{}: {}".format(city_inst.id, city_inst.name))
