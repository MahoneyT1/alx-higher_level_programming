#!/usr/bin/python3

"""
Write a script that lists all State objects from the database `hbtn_0e_6_usa`
script takes three arguments `username`, `password` `db_name`

it connects to mysql server on `localhost` on `port3306`
returns in ascending order by `states.id`
cold should not be executed when imported
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    conString = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                                                                argv[1],
                                                                argv[2],
                                                                argv[3])

    engine = create_engine(conString)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f'{state.id}: {state.name}')

    session.close()
