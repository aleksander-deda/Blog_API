from pydantic import BaseModel
from typing import List


class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    class Config():         # Because we are using a db query at main.py so it needs to be True
        orm_mode = True


class User(BaseModel):
    name: str
    email: str 
    password: str


class ShowUser(BaseModel):
    name: str 
    email: str
    blogs: List[Blog] = [] 

    class Config():         
        orm_mode = True


class ShowBlog(BaseModel):
    title: str 
    body: str 
    creator: ShowUser
    
    class Config():
        orm_mode = True