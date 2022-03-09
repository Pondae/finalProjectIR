
from flask import Flask, request, jsonify
from flask_cors import cross_origin
from Recipe_dev import *


app = Flask(__name__)


@app.route("/title_name", methods=["POST"])
@cross_origin()
def Title():
    return jsonify(SearchingByTitle(request.json['query']))


@app.route("/ingredients", methods=["POST"])
@cross_origin()
def Ingredient():
    return jsonify(SearchingByIngredients(request.json['query']))


@app.route("/mark_search", methods=["POST"])
@cross_origin()
def Mark_Search():
    return jsonify(Searching_mark(request.json['query']))


@app.route("/Login", methods=["POST"])
@cross_origin()
def Login():
    username = request.json['username']
    password = request.json['password']
    print(username)
    print(password)

    return jsonify(Login_user(username, password))


@app.route("/get_mark_data", methods=["GET"])
@cross_origin()
def GettingMark_data():
    return jsonify(Getmark_data())


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
    print('Adding mark fav: ' + str(title) + 'and ' + str(recipe))
    return 'Adding mark fav: ' + str(title) + 'and ' + str(recipe)


@app.route("/unmark_data", methods=["POST"])
@cross_origin()
def UnMark_data():
    identify = request.json['id']
    cursor = db.cursor()
    sql = '''
    DELETE FROM `foodrecipe`.`fav_recipe` WHERE (`id_fav_recipe` = %s );
    '''
    cursor.execute(sql, (identify,))
    print('Deleting mark fav: ' + str(identify))
    return 'Deleting mark fav: ' + str(identify)


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
