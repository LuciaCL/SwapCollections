# Flask handlers to create, update, delete users
# POST /users/ with json (create a user)

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')


def post_user(user):
    print("First line in post_user()")
    db = client.pymongo_test
    db = client['pymongo_test']

    result = db.users.insert_one(vars(user))
    print('One post: {0}'.format(result.inserted_id))
    return result.inserted_id


def update_user(user_id, user):
    pass
