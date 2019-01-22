# Flask handlers to create, update, delete users
# POST /users/ with json (create a user)

from pymongo import MongoClient
import re

client = MongoClient('mongodb://localhost:27017')
db = client['pymongo_test']
collection = db.users


def post_user(user):
    print("First line in post_user()")
    db = client.pymongo_test

    if validations_user(user):
        db.users.insert_one(vars(user))
        user._id = str(user._id)
        return user
    else:
        print('Error in the validation')
        return False


def update_user(user_id, changes):
    db.users.update_one({'_id': user_id}, {"$set": changes}, upsert=False)


def delete_user(user_id):
    db.users.delete_one({'_id': user_id})


def validations_user(user):

    # TODO password_match(user.password,user.re_)

    if user.user_name is None or user.first_name is None or user.last_name is None or user.password is None:
        return False

    email_to_verify = user.email
    match = re.match('^[_a-z0-9-]+(\\.[_a-z0-9-]+)*@[a-z0-9-]+(\\.[a-z0-9-]+)*(\\.[a-z]{2,4})$', email_to_verify)

    if match is None:
        return False
    else:
        return True
