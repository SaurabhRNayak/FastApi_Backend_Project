from fastapi import Request,HTTPException
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from .jwtHandler import decodeJWT
class jwtBearer(HTTPBearer):
    def __init__(self,auto_Error:bool=True,):
        super(jwtBearer,self).__init__(auto_error=auto_Error)

    async def __call__(self, request: Request) :
        credentials:HTTPAuthorizationCredentials = await super(jwtBearer,self).__call__(request)
        print(credentials)
        if credentials:
            if not credentials.scheme=="Bearer":
                raise HTTPException(status_code=403,detail="Invalid or Expired Token")
            if not self.verifyJWT(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403,detail="Invalid or Expired Token")
    
    def verifyJWT(self,jwtToken:str):
        payload = decodeJWT(jwtToken)
        return True if payload  else False