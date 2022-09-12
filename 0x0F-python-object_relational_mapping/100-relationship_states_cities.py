#!/usr/bin/python3
"""
A script that creates the State “California”
with the City “San Francisco” from
the database hbtn_0e_100_usa
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    san_francisco = City("San Francisco")
    california = State("California", [san_francisco])

    session.add(california)
    session.commit()
    session.close()
