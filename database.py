import pymongo
from config import MONGO_URI

client = pymongo.MongoClient(MONGO_URI)
db = client['TeraboxBot']
users = db['users']

def add_user(user_id):
    if not users.find_one({"user_id": user_id}):
        users.insert_one({"user_id": user_id})

def check_user(user_id):
    return users.count_documents({})  # Return total user count
