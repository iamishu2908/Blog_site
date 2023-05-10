from fastapi import FastAPI
from database import models
from database.database import engine
from routers import post
from fastapi.staticfiles import StaticFiles
app = FastAPI()

app.include_router(post.router)


models.Base.metadata.create_all(engine) # this is not related with schemas.py
'''
    This line creates all the tables defined in the SQLAlchemy ORM models in the database specified by the engine instance. 
    This is useful when you want to initialize or update the database schema based on changes made to the models in the code.
'''
    # models: This is the module that contains the SQLAlchemy ORM models, which are Python classes that define the database tables and their relationships.
    # Base: This is the instance of the declarative_base class that was created in the models module, which is used to create the database schema.
    # metadata: This is a collection of metadata about the database schema, such as table names and column types, which is attached to the Base instance.
    # create_all(): This is a method of the metadata object that creates all the tables defined in the metadata object.
    # engine: This is the instance of the create_engine class that represents the database connection, which is used to execute SQL statements to create the tables in the database.

app.mount('/images', StaticFiles(directory= 'images'),name = 'images')
#  maps a URL path to a static directory in order to serve static files to the client.
# When a request is made to the '/images' URL path, the ASGI server will serve the corresponding file from the directory located at './images'