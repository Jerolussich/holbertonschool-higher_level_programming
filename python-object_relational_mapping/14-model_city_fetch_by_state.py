#!/usr/bin/python3

from model_city import City
from model_state import Base, State
from sqlalchemy import select, join, asc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv
                                                                            [1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(engine)
    session = Session()

    results = session.query(State, City).join(
        City).order_by(asc(City.id)).all()

    for state, city in results:
        print("{}: ({}) {}".format(
            state.name, city.id, city.name))

    session.close()
