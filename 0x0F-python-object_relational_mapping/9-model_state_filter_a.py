#!/usr/bin/python3
"""
 lists all State objects from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    from model_state import State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    import sys

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    engine.connect()

    session = Session(engine)

    for state in session.query(State).order_by(State.id).all():
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))

    session.close()
