from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime
from pydantic.types import conint

# The pydantic module allows us to make models for requests and responses

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class User(BaseModel):
    id: int
    email: str
    created_at: datetime

    class Config():
        from_attributes = True

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: User

    class Config():
        # convert ORM content to response
        from_attributes = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config():
        from_attributes = True

class UserCreate(BaseModel):
    email: EmailStr()
    password: str

class UserLogin(BaseModel):
    email: EmailStr()
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)