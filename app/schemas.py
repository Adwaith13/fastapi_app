from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    email:EmailStr
    password:str

class UserGet(BaseModel):
    id:int
    email:str
    created_at:datetime
    
    class Config:
        orm_mode = True   
        
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[str] = None
    
class PostCreate(BaseModel):
    title:str
    content:str
    
    
class PostGet(BaseModel):
    id:int
    title:str
    content:str
    created_at:datetime
    owner_id:int
    owner:UserGet
    
    class Config:
        orm_mode = True
    
    