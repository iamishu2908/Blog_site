'''
This code sets up a database connection using SQLAlchemy, a popular Object Relational Mapping (ORM) tool.
SQLAlchemy is a library that facilitates the communication between Python programs and databases. 
Most of the times, this library is used as an Object Relational Mapper (ORM) tool that translates Python classes to tables on relational databases and automatically converts function calls to SQL statements.
Using SQLAlchemy, we have no restriction on what db to use for our project.

'''
from sqlalchemy import create_engine # This function is used to create a database engine, which handles the connection to the database and execution of SQL commands.
from sqlalchemy.ext.declarative import declarative_base # This function is used to create a base class for declarative SQLAlchemy models.
from sqlalchemy.orm import sessionmaker # This function is used to create a session factory, which creates new sessions to interact with the database.
 
SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog_api.db' # This sets the database URL to a SQLite database file named blog_api.db in the current directory.
 
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}) # This creates a database engine with the given database URL and passes a keyword argument to disable thread checking. The engine is used to create connections to the database.
 
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False) # This creates a session factory with the given database engine and sets autocommit and autoflush to False. The session factory is used to create new sessions to interact with the database.
 
Base = declarative_base() # This creates a base class for declarative SQLAlchemy models.
 
def get_db():
    db = SessionLocal() # This creates a new session using the session factory defined earlier.
    try:
        yield db
    finally:
        db.close()

'''Overall, this code sets up a SQLite database connection using SQLAlchemy and provides a function get_db() that returns a database session object.
 The session object can be used to query and manipulate the database in a Pythonic way using SQLAlchemy's ORM capabilities.'''