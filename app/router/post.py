from fastapi import FastAPI,HTTPException,status,Depends,APIRouter
from sqlalchemy.orm import Session
from .. import models,schemas,oauth2
from ..database import get_db
from typing import List

router  = APIRouter(prefix="/posts",tags=["Posts"])

@router.post("/",response_model=schemas.PostGet,status_code=status.HTTP_201_CREATED)
def create_post(post:schemas.PostCreate,db:Session=Depends(get_db),current_user_id:int = Depends(oauth2.get_current_user)):
    new_post = models.Post(owner_id = current_user_id.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post

@router.get("/",response_model=List[schemas.PostGet],status_code=status.HTTP_200_OK)
def get_posts(db:Session=Depends(get_db)):
    posts = db.query(models.Post).all()
    
    return posts
    
