#!/usr/bin/python3


"""
Write a python file that contains the class definition of a State
and an instance
`Base` = `declarative_base()`

Inherits from `Base`
class attributes `id` not nul auto generate `id`
class attritube `name` `nollable = false`
must `import MySQLAlchemy`
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from sys import argv

Base = declarative_base()


class State(Base):
    """ inherited base """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column('name', String(128), nullable=False)
