import json

from flask import Flask, request, jsonify
from flask_cors import cross_origin
from Login import *

app = Flask(__name__)


@app.route("/Login", methods=["POST"])
@cross_origin()
def Login():
    return Login(request.json['username'], request.json['password'])


@app.route("/", methods=["GET"])
@cross_origin()
def HI():
    return "hi"


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
