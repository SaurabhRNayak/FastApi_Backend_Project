from turtle import st
from fastapi import APIRouter,Body
from models.auth import UserSchema,UserLoginSchema
authRoot = APIRouter()
from Auth.jwtHandler import signJWT,decodeJWT

USERS=[]

@authRoot.post("/user/signup",tags=["Auth"])
def userSignUp(userInfo:UserSchema=Body()):
    USERS.append(userInfo)
    return signJWT(userInfo.email)

@authRoot.post("/user/login",tags=["Auth"])
def userSignUp(userInfo:UserLoginSchema=Body()):
    if(checkUser(userInfo)):
        return signJWT(userInfo.email)
    else:
        return({
            "Error":"Invalid credentials or Not a user"
        })

def checkUser(userInfo:UserLoginSchema):
    for user in USERS:
        if user.email == userInfo.email and user.password==userInfo.password:
            return True
        else:
            return(False)
