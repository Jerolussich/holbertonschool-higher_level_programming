#!/usr/bin/python3

from model_state import Base, State
from sqlalchemy import select
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv
                                                                            [1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).order_by(State.id.asc()).all()

    for item in state:
        print("{}: {}".format(item.id, item.name))
