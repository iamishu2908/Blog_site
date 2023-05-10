from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel): # this schema shows what you can extract from an api request 
    # Note : Post method and Posts (blog) are different
    title: str
    content: str
    image_url: str
    creator: str

class PostDisplay(BaseModel): #  this schema displays how the PostBase information is stored in the api
    id: int
    title: str
    content: str
    image_url: str
    creator: str
    timestamp: datetime
    class Config(): # we define this here so that the stuff in database gets mapped with this format
        # ORM - Object Relational Mapping
        orm_mode = True

