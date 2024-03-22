#!/usr/bin/python3
"""
Write a script that adds the State object “Louisiana” to the database
The script takes three argument `username` `password` `database_name`

The script prints states.id after creation
also it doesn't execute when imported
"""

import sqlalchemy
from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sys import argv

if __name__ == '__main__':
    # check if total entered input from argv == 4
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

    # obj to create
    new_state = State(name="Louisiana")

    # add to session
    session.add(new_state)

    # commit the session
    session.commit()
    print(new_state.id)
    session.close()
