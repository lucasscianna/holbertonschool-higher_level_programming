#!/usr/bin/python3
"""
Lists all State objects that contain the letter a
from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def filter_a():
    """
    Connects to the database and retrieves states containing 'a'.
    """
    if len(sys.argv) == 4:
        user = sys.argv[1]
        passwd = sys.argv[2]
        db_name = sys.argv[3]

        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                user, passwd, db_name),
            pool_pre_ping=True
        )

        Session = sessionmaker(bind=engine)
        session = Session()

        states = session.query(State).filter(State.name.contains('a'))\
            .order_by(State.id).all()

        for state in states:
            print("{}: {}".format(state.id, state.name))

        session.close()


if __name__ == "__main__":
    filter_a()