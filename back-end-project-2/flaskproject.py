from flask import Flask, request, jsonify
from flask_cors import cross_origin
from Recipe_dev import *
# import json
# import mysql.connector
#
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="0808601871",
#     database='foodrecipe'
# )

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


@app.route("/get_mark_data/<int:userid>", methods=["GET"])
@cross_origin()
def GettingMark_data(userid):
    return jsonify(Getmark_data(userid))


@app.route("/mark_data", methods=["POST"])
@cross_origin()
def Mark_data():
    title = request.json['title']
    recipe = request.json['recipe']
    image = request.json['image']
    userid = request.json['userid']
    fav_id = []
    cursor = db.cursor()
    sql = '''
    INSERT INTO `foodrecipe`.`fav_recipe` ( `title`, `recipe`, `image`) VALUES (%s, %s, %s);
    '''
    val = (title, recipe, image)
    cursor.execute(sql, val)
    sql_latest_id = '''
        SELECT id_fav_recipe FROM fav_recipe ORDER BY id_fav_recipe DESC LIMIT 1; 
    '''
    cursor.execute(sql_latest_id)
    result = cursor.fetchall()
    for i in result:
        val = json.dumps(i)
        fav_id.append(val.translate(str.maketrans('', '', '([$\'_&+\n?@\[\]#|<>^*()%\\!"-\r\])' + U'\xa8')))

    tamp = fav_id[0]
    sql_insert_mid = '''
        INSERT INTO `foodrecipe`.`user_with_fav` ( `id_fav_recipe`, `id_user`) VALUES (%s, %s);
        '''
    val2 = (tamp, userid)
    cursor.execute(sql_insert_mid, val2)
    fav_id.pop()
    # db.commit()

    print('user id: ' + str(userid) + ' Adding mark fav: ' + str(title) + 'and ' + str(recipe) + 'and ' + str(image))
    return 'user id: ' + str(userid) + ' Adding mark fav: ' + str(title) + 'and ' + str(recipe) + 'and ' + str(image)


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
