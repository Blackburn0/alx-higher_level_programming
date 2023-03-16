#!/usr/bin/python3
'''Lists out all the contents of the 'State' table to the screen
'''
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'\
        .format(username, password, db_name)
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    # Creating a new session
    session = Session()
    objs = session.query(State).order_by(State.id).all()
    for obj in objs:
        print('{}: {}'.format(obj.id, obj.name))
