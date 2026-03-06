#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def fetch_first_state():
    """
    Connects to the database and retrieves the first state by id.
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

        first_state = session.query(State).order_by(State.id).first()

        if first_state:
            print("{}: {}".format(first_state.id, first_state.name))
        else:
            print("Nothing")

        session.close()


if __name__ == "__main__":
    fetch_first_state()