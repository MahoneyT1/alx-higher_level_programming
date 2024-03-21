#!/usr/bin/python3

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, create_engine
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    username = Column(String(25), nullable=False, unique=True)
    email = Column(String(25), nullable=False, unique=True)
    date_created = Column(DateTime(), default=datetime.utcnow)

    def __repl__(self):
        return f"{self.username} {self.email} {self.date_created}"


new_user = User(id=1, username='mahoney', email='ifeanyi@gmail.com')
print(new_user)

cnns = 'mysql://root:Drew2325$$@localhost/testdatabase'

engine = create_engine(cnns, echo=True)
