from database import db_post
from fastapi import APIRouter, Depends
from routers.schemas import PostBase, PostDisplay
from sqlalchemy.orm import Session
from database.database import get_db

router = APIRouter(
    prefix = '/post',
    tags = ['post']
)

@router.post('') # passing empty string bcoz router prefix is /post already
def create(request: PostBase, db: Session = Depends(get_db)):
    return db_post.create(db,request)

@router.get('/all')
def get_all_posts(db: Session = Depends(get_db)):
    return db_post.get_all(db)

@router.delete('/{id}')
def delete(id:int,db:Session=Depends(get_db)):
    return db_post.delete(id,db)


