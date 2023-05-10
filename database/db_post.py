from routers.schemas import PostBase # to add data to db
from sqlalchemy.orm.session import Session
import datetime
from database.models import DbPost

#   Create new post

def create(db: Session, request: PostBase):
    new_post = DbPost(
        image_url = request.image_url,
        title = request.title,
        content = request.content,
        creator = request.creator
        timestamp = datetime.datetime.now()
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post) # to capture the id that is automatically generated by db after a create request
    return new_post
