
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
   print("Hello is executed!")
   return jsonify({'user' : 'David'})


if __name__ == '__main__':
   app.run(debug=True)
