# app/database.py

import os
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv

# 1. Load environment variables from .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# 3. Create the SQLModel/SQLAlchemy engine
# Think of it as a connection factory and pool manager. 
# Whenever you run a query, SQLAlchemy/SQLModel asks the engine for a connection from its pool, 
# sends SQL to the database, and returns results
engine = create_engine(DATABASE_URL, echo=True)  

"""
What Sessions does?
Under the hood, calling session.add(...) or running a query causes the Session to grab a connection
from the engine, send SQL, and keep track of any objects you're working with.
get_session is a generator just to make a new sessions each time we are using the get_session
function, abd as soon as the request is completed, it closes automatically instead of writing 
db = Session(engine); …; db.close() all the time.
"""
def get_session() -> Session: # type: ignore
    with Session(engine) as session:
        yield session

# Creating all the tables registered in models.py since it gets all the infromation from the metadata
# that is saved on SQLMODEL (a parameter you add to each class), therefore it knows to go over all of them
# and create them
def create_tables():
    SQLModel.metadata.create_all(engine)
