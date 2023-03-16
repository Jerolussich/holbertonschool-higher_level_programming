#!/usr/bin/python3
"""script that deletes all State objects with a name containing\
    the letter a from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy import select
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(engine)
    session = Session()

    state = session.query(State).filter(State.name.contains("a")).delete()
    session.commit()

    session.close()
