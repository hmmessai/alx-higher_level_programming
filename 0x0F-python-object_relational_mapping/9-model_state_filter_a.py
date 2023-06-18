#!/usr/bin/python3
"""Lists all State objectss that contain the letter a from the db"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instances = (session.query(State)
                        .filter(State.name.like('%a%'))
                        .order_by(State.id))
    for instance in instances:
        print(instance.id, instance.name, sep=": ")
