#!/usr/bin/python3

"""
 script that prints the first State object from the database hbtn_0e_6_usa

 must import the module ` SQLAchemy`
 import `State` `Base` from `model_state`
 it connects to `mysql` server running on `localhost` on port `3306`

 not allowedto fetch all states from the database before displaying
 if the table states is empty, print nothing followed by a new line
 doesnt execute when imported

"""

from sqlalchemy import create_engine, Column, String, Integer
import sqlalchemy
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':
    # create a connectiong string
    conString = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                                                                  argv[1],
                                                                  argv[2],
                                                                  argv[3]
                                                                  )
    # create the engine
    engine = create_engine(conString)

    # create a session and bind engine to it
    Session = sessionmaker(bind=engine)

    # create an instance of session class
    session = Session()

    # create a querry
    result = session.query(State).order_by(State.id).first()

    if result:
        print("{}: {}".format(result.id, result.name))
    else:
        print('Nothing')
