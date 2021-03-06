from pymongo import MongoClient
from bson.objectid import ObjectId
from app.user.user import *
client = MongoClient('mongodb://localhost:27017')
db = client['pymongo_test']


def insert_user(user):

	result = db.users.insert_one(vars(user))
	return result.inserted_id


def search_by_id(user_id):

	user_id_string = str(user_id)
	return db.users.find_one({"_id": ObjectId(user_id_string)})
