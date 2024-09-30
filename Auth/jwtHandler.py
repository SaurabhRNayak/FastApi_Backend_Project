import time
import jwt
from decouple import config
from dotenv import dotenv_values

conf = dotenv_values('.\config\.env')
JWT_SECRET = conf["AUTHSECRET"]
JWT_ALGORITHM = conf["AUTHALGORTHM"]

def tokenResponse(token:str):
    return{
        "access_token":token
    }

def signJWT(userID:str):
    payload={
        "userID":userID,
        "expiry":time.time()+600
    }

    token=jwt.encode(payload,JWT_SECRET,algorithm=JWT_ALGORITHM)
    return(tokenResponse(token))

def decodeJWT(token):
    try:
        decodedVal=jwt.decode(token,JWT_SECRET,algorithms=[JWT_ALGORITHM])
        return decodedVal if decodedVal['expiry']>time.time() else None
    except Exception as e:
        print(e)
        return{}
