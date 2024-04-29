from fastapi import APIRouter,HTTPException,Depends,status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User
from ..schemas import UserCreate,UserGet
from ..utils import hash

router = APIRouter(prefix="/users",tags=['Users'])

@router.post("/", response_model=UserGet, status_code=status.HTTP_201_CREATED)
def create_user(user:UserCreate,db:Session=Depends(get_db)):
    hashed_password = hash(user.password)
    user.password = hashed_password
    
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user
    
    
@router.get("/{id}",status_code=status.HTTP_200_OK,response_model=UserGet)
def get_user(id:int,db:Session=Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="""user 
                            not found with {id} id """)
    
    return user
    


