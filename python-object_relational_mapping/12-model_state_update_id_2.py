#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa.
Updates the state where id = 2 to 'New Mexico'.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def update_state():
    """
    Connects to the database and updates a specific state name by id.
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

        state_to_update = session.query(State).filter(State.id == 2).first()

        if state_to_update:
            state_to_update.name = "New Mexico"
            session.commit()

        session.close()


if __name__ == "__main__":
    update_state()