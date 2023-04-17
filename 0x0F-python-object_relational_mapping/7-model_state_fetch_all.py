#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""
from sqlalchemy import (create_engine)
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    s = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.\
        format(user, password, dbname)

    engine = create_engine(s, echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    states = Session()

    for state in states.query(State).order_by(State.id):
        print(state.id, state.name, sep=": ")
