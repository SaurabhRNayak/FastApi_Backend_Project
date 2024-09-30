from lib2to3.pytree import Base
from pydantic import BaseModel,Field,EmailStr


class UserSchema(BaseModel):
    name :str = Field(default=None)
    email:EmailStr=Field(default=None)
    password:str=Field(default=None)
    class Config:
        the_schema = {
            "DEMO USER":{
                "name":"Sherlock",
                "email":"sherlock@watson.com",
                "password":"DID YOU MISS ME!!"
            }
        }
class UserLoginSchema(BaseModel):
    email:EmailStr=Field(default=None)
    password:str=Field(default=None)
    class Config:
        the_schema = {
            "DEMO USER":{
                "email":"sherlock@watson.com",
                "password":"DID YOU MISS ME!!"
            }
        }