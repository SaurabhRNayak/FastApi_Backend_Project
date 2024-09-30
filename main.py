from fastapi import FastAPI
from routes.here import entry_root 
from routes.blog import blog_root
from routes.auth import authRoot
app = FastAPI()


app.include_router(entry_root)
app.include_router(blog_root)
app.include_router(authRoot)