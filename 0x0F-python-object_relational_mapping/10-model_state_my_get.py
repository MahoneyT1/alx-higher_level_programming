#!/usr/bin/python3

"""
a script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa

The script takes 4 arguments `mysql-username` `password` `database_name`
`and state name to search`

returns states.id

if no state has the name provided it prints `Not found`
connects on `localhost` on port `3306`

"""

import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import State, Base


if __name__ == '__main__':
    # check if number of argv is not up to 4
    if len(argv) != 5:
        print("Usage: < username > < password > < db name >\
                                     < state name search >")
        exit(1)

    conString = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                                                                argv[1],
                                                                argv[2],
                                                                argv[3]
                                                                )
    # create an engine
    engine = create_engine(conString)

    # create an instance of session
    Session = sessionmaker(bind=engine)

    # create an obj of Session()
    session = Session()

    # store the collected data here
    state_name = argv[4]

    result = session.query(State).filter(State.name == state_name
                                         ).order_by(State.id)

    # check if result is availabe or found in the database print this
    if result:
        for r in result:
            print(r.id)
            exit()
    print("Not found")

    session.close()
