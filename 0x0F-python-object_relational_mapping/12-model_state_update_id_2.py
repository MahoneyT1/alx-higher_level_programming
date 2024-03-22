#!/usr/bin/python3

"""
a script that changes the name of a State object from a database

script takes 3 argument `username` `password` `database_name`from mode'
connects to mysql server on `localhost` on port `3306`
changes the name of the `State` to `new mexico`
with the `id`
script doesn't work when imported

"""

import sqlalchemy
from sqlalchemy import create_engine, String, Integer
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == '__main__':
    # check if input is == 4
    if len(argv) != 4:
        print("Usage: < username > < password > < db name >")
        exit(1)

    # connection string
    conString = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                                                                argv[1],
                                                                argv[2],
                                                                argv[3]
                                                                )
    # create engine
    engine = create_engine(conString)

    # create a session and bind the engine with the sessionmaker
    Session = sessionmaker(bind=engine)

    # create an instance of Session()
    session = Session()

    result = session.query(State).filter(State.id == 2).first()

    if result:
        result.name = "New Mexico"
        session.add(result)
        session.commit()

    session.close()
