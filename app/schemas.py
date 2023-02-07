from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title :  str
    content : str
    published : bool = True
   
class UserBase(BaseModel):
    email : EmailStr
    password : str
    
class CreatePost(PostBase):
    pass

class CreateUser(UserBase):
    pass

class User(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True

class Post(PostBase):
   id: int
   created_at: datetime
   owner_id : int
   owner : User
   class Config:
       orm_mode = True

class Ride(BaseModel):
    id : int
    going_to: str
    coming_from : str
    class Config:
        orm_mode = True

class Provider(BaseModel):
    id : int
    name: str
    address: str
    email: EmailStr
    class Config:
        orm_mode= True
    
class CreateProvider(Provider):
    password: str

    

class UpdateUserPassword(BaseModel):
    password: str

class UpdateUserEmail(BaseModel):
    email:EmailStr

class UserLogin(BaseModel):
    email : EmailStr
    password : str

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id: str = None