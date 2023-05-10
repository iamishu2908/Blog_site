from database import db_post
from fastapi import APIRouter, Depends,UploadFile, File
from routers.schemas import PostBase, PostDisplay
from sqlalchemy.orm import Session
from database.database import get_db
import string
import random
import shutil

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

@router.post('/image')
def upload_image(image: UploadFile = File(...)):
    # images will be stored in db, so their file names should be unique as same images shudnt be having same names
    letter = string.ascii_letters # gives us all ascii letters
    rand_str = ''.join(random.choice(letter) for i in range(6))# generates 6 random letters and appends to string
    new = f'_{rand_str}.'
    filename = new.join(image.filename.rsplit('.', 1)) # adding rand_strat the end of actual image url
    path = f'images/{filename}' # path used to store filenames of images

    with open(path, "w+b") as buffer: # write a file and over write it as buffer
        shutil.copyfileobj(image.file, buffer) # store file

    return {'filename': path}




