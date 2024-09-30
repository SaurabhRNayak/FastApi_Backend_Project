from fastapi import APIRouter

entry_root = APIRouter()


@entry_root.get("/",tags=["Test"])
def apiRunning():
    res={
        "status":"ok",
        "message":"API is running"
    }
    return res
