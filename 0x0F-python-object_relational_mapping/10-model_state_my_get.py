#!/usr/bin/python3
"""
 lists all State objects from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    import sys
    search = False

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    engine.connect()

    session = Session(engine)

    for state in session.query(State).all():
        if sys.argv[4] == state.name:
            print("{}".format(state.id))
            search = True
    if search is False:
        print("Not found")
    session.close()
