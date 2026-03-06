#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_state():
    """
    Connects to the database and searches for a specific state name.
    """
    if len(sys.argv) == 5:
        user = sys.argv[1]
        passwd = sys.argv[2]
        db_name = sys.argv[3]
        state_name = sys.argv[4]

        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                user, passwd, db_name),
            pool_pre_ping=True
        )

        Session = sessionmaker(bind=engine)
        session = Session()

        state = session.query(State).filter(State.name == state_name).first()

        if state:
            print("{}".format(state.id))
        else:
            print("Not found")

        session.close()


if __name__ == "__main__":
    get_state()