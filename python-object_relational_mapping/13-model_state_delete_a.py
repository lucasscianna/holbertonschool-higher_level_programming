#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def delete_states():
    """
    Connects to the database and deletes states containing 'a'.
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

        states_to_del = session.query(State).filter(State.name.contains('a'))

        for state in states_to_del:
            session.delete(state)

        session.commit()
        session.close()


if __name__ == "__main__":
    delete_states()