import json

from flask import Flask, request, jsonify
from flask_cors import cross_origin
from Recipe_dev import *


app = Flask(__name__)


@app.route("/Login", methods=["POST"])
@cross_origin()
def Login():
    username = request.json['username']
    password = request.json['password']
    print(username)
    print(password)
    check = Loginuser(username, password)
    output = json.dumps(check)
    return output


@app.route("/", methods=["GET"])
@cross_origin()
def HI():
    return "hi"


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
