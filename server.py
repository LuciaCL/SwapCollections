from flask import Flask
from flask import jsonify
import app.user.user_handler

server_app = Flask(__name__)


@server_app.route('/hello', methods=['GET'])
def hello():
    print("Hello is executed!")
    result = app.user.user_handler.post_user()
    print(result)
    return jsonify({'user': 'algo'})


if __name__ == '__main__':
    server_app.run(debug=True)
