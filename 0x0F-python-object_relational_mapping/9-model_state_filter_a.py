#!/usr/bin/python3

"""
a script that lists all State objects that contain the letter a from the
database

This script takes three argument `username`, `password` `database_name`
it connects to `MySQL + MyQLdb` running on `localhost` on port `3306`
The result is returned on ascending order
Script doesn't run when imported

"""
# importing the dependacies on sqlAlchemy

import sqlalchemy
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == '__main__':
    # check if argv is not up to required input

    if len(argv) != 4:
        print("Usage: < name of file > < mysql-username > < mysql-password >\
              < database_name >")

        exit(1)

    # Creating connection string
    conString = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                                                                argv[1],
                                                                argv[2],
                                                                argv[3]
                                                                )
    # create engine
    engine = create_engine(conString)

    # create a session by using the sessionmaker method and bind engine with it
    Session = sessionmaker(bind=engine)

    # create an instance of Session()
    session = Session()

    # create a query that will list all state object that contains a
    # like method is a column method
    result = session.query(State).filter(State.name.like("%a%")).\
        order_by(State.id).all()

    # loop through the returned result
    for r in result:
        print("{}: {}".format(r.id, r.name))
