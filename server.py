from flask import Flask
from flask import jsonify
from flask import request

from app.user.parameter_reader import parse_user_from_request
from app.user.password_utils import *
from app.user.user_handler import post_user

#from flask_jwt_extended import JWTManager

server_app = Flask(__name__)


@server_app.route('/users', methods=['POST'])
def create_user():

    # TODO find a module to run embedded mongo to run the test.
    # TODO fin how to generate a swagger documentation.
    # TODO find a library for managing tokens ,(jwt, oauth)

    user_view = parse_user_from_request(request)
#:TODO: REVIEW THIS IF

    if password_match(user_view.password, user_view.re_password) :
        inserted_user = post_user(user_view.to_user())
        inserted_user.password = ''
        # Send the user created
        return jsonify(inserted_user.__dict__)
    else:
        print('Password incorrect')
        return 'Password incorrect'


@server_app.route('/users/<user_id>', methods=['GET'])
def get_user_by_id(user_id):
    # get user by id
    pass


@server_app.route('/users', methods=['GET'])
def get_user_by_email():
    # here we want to get the value of user (i.e. ?user=some-value)
    email = request.args.get('email')
    # get user by email
# One more for get user by user name.


@server_app.route('/users', methods=['GET'])
def get_users():
    # pagination, CHECK HOW TO HAVE A DIFFERENCE BETWEEN GET_USERS AND GET_USER_BY_ID
    pass


@server_app.route('/users/<user_id>', methods=['DELETE'])
def delete_user_by_id(user_id):
    pass


if __name__ == '__main__':
    server_app.run(debug=True)
