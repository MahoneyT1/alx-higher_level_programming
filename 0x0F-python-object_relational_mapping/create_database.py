#!/usr/bin/python3

from example import User, engine, Base
from sqlalchemy.orm import sessionmaker
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

fresh = User(username="ifeanyi", email="ifeanyi@gmail.com")

session.add(fresh)

session.commit()


