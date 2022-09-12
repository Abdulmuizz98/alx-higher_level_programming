#!/usr/bin/python3
"""
A script that lists all State objects
from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    """
    cities = session.query(City) \
        .join(State) \
        .filter(City.state_id == State.id).all()
    `"""
    cities = session.query(State, City) \
        .filter(City.state_id == State.id).all()
    [print(f'{state.name}: ({city.id}) {city.name}') for state, city in cities]
