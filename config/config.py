
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv,dotenv_values
import os

conf = dotenv_values('.\config\.env')

uri = "mongodb+srv://Saurabh:{password}@atlasmon.okaf4.mongodb.net/?retryWrites=true&w=majority&appName=AtlasMon".format(password=conf['ATLAS_PASSWORD'])

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.Blogging
blogs_collection = db["blogs"]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)