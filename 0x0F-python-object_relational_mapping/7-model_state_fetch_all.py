#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""
from sqlalchemy import (create_engine)
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
import sys

user = sys.argv[1]
password = sys.argv[2]
dbname = sys.argv[3]
if __name__ == '__main__':
    connection_string = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, password, dbname)

    engine = create_engine(connection_string, echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    states = Session()

    for state in states.query(State).order_by(State.id):
        print(state.id, state.name, sep=": ")
