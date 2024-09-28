from pydantic import BaseModel

class BlogModel(BaseModel):
    title:str
    subTitle:str
    content:str
    tags:list

class UpdateBlogModel(BaseModel):
    title:str=None
    subTitle:str=None
    content:str=None
    tags:list=None
    