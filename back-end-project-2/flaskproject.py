import json

from flask import Flask, request, jsonify
from flask_cors import cross_origin
from Recipe_dev import *
import mysql.connector

app = Flask(__name__)


@app.route("/title_name", methods=["POST"])
@cross_origin()
def Title():
    return jsonify(SearchingByTitle(request.json['query']))


@app.route("/ingredients", methods=["POST"])
@cross_origin()
def Ingredient():
    return jsonify(SearchingByIngredients(request.json['query']))


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


# @app.route("/", methods=["GET"])
# @cross_origin()
# def HI():
#     return "hi"


@app.route("/mark_data", methods=["POST"])
@cross_origin()
def Mark_data():
    title = request.json['title']
    recipe = request.json['recipe']
    cursor = db.cursor()
    sql = '''
    INSERT INTO `foodrecipe`.`fav_recipe` ( `title`, `recipe`) VALUES (%s, %s);
    '''
    val = (title, recipe)
    cursor.execute(sql, val)
    db.commit()
    return 'hi'


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
