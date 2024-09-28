from bson import objectid
def decodeBlog(data)->dict:
    return(
        {"_id":str(data["_id"]),
        "title":data['title'],
        "subTitle":data['subTitle'],
        "content":data['content'],
        # "author":data['author'],
        "date":data["date"]}
        )
    

def decodeAllBlog(data)->list:
    return(decodeBlog(blog) for blog in data)

