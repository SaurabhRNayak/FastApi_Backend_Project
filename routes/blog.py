from turtle import st
from fastapi import APIRouter,Depends
from Auth.jwtBearer import jwtBearer
from models.blog import BlogModel,UpdateBlogModel
blog_root = APIRouter()
from config.config import blogs_collection
from serializers.blog import decodeAllBlog,decodeBlog
import datetime
from typing import Optional
from bson import ObjectId

@blog_root.post("/new/Blog",dependencies= [Depends(jwtBearer())],tags=["Blog"])
def newBlog(data:BlogModel):
    dataDict = dict(data)
    dataDict['date']=str(datetime.date.today())

    postResponse = blogs_collection.insert_one(dataDict)
    dataId=str(postResponse.inserted_id)
    return({
        "status":"ok",
        "message":"New Blog inserted",
        "_id": dataId
    })

@blog_root.get("/all/blogs",tags=["Blog"])
def getAllBlog():
    print("qwertyuiol;")
    getresponse = blogs_collection.find()
    print(getresponse)
    decodedData = decodeAllBlog(getresponse)

    return({
        "status":"ok",
        "data":decodedData
    })


@blog_root.get("/blogs/by-title/{title}",tags=["Blog"])
@blog_root.get("/blogs/by-id/{blog_id}",tags=["Blog"])
def get_filtered_blogs_route(title: Optional[str] = None, blog_id: Optional[str] = None):
    filter_query = {}

    # Filter by name if provided
    if title:
        try:
            getResponse = blogs_collection.find({"title":{"$regex": f".*{title}.*", "$options": "i"}})
            decodedData = decodeAllBlog(getResponse)

            return({
                "status":"ok",
                "data":decodedData
            })
        except Exception as e:
            return {"status": "error", "message": f"filterByName error: {e}"}
    # Filter by _id if provided and is a valid ObjectId
    if blog_id:
        try:
            getResponse = blogs_collection.find({"_id":ObjectId(blog_id)})
            decodedData = decodeAllBlog(getResponse)

            return({
                "status":"ok",
                "data":decodedData
            })
        except Exception as e:
            return {"status": "error", "message": f"filterById error: {e}"}

    return {"status": "error", "message": f"filter error: {e}"}

@blog_root.patch("/update/{_id}",tags=["Blog"])
def updateBlog(id:str,data:UpdateBlogModel):
    dictData = dict(data.model_dump(exclude_unset=True))
    patchResponse=blogs_collection.find_one_and_update(
        {"_id":ObjectId(id)},{"$set":dictData}
    )
    return({
                "status":"ok",
                "message":"Updated one blog successfully"
            })

@blog_root.delete("/delete/{_id}",tags=["Blog"])
def updateBlog(id:str):
    patchResponse=blogs_collection.delete_one(
        {"_id":ObjectId(id)}
    )
    return({
                "status":"ok",
                "message":"Deleted one blog successfully"
            })