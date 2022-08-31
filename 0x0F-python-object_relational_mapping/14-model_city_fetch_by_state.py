#!/usr/bin/python3
"""
 lists all State objects from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    import sys

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    engine.connect()

    session = Session(engine)

    for city, state in session.query(City, State).\
            filter(City.state_id == State.id).order_by(City.id):
        print(f"{state.name}: ({city.id}) {city.name}")
