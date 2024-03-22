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
import sqlalchemy

metadata = sqlalchemy.MetaData()

Base = declarative_base(metadata=metadata)


class State(Base):
    """ creating the structure of our table, State inheriting from base """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column('name', String(128), nullable=False)
