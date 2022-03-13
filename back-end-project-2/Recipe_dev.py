import json
import string
# pip install mysql-connector
import mysql.connector
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

from spellchecker import SpellChecker

spell = SpellChecker()

a = spell.correction("purk")

data = pd.read_csv('resource/Food_ingredients.csv')
data.drop_duplicates()

data['Title'] = data['Title'].astype(str)
data['Title'] = data['Title'].apply(lambda s: s.translate(str.maketrans('', '', string.punctuation + u'\xa0')))
data['Title'] = data['Title'].apply(lambda s: s.lower())
data['Title'] = data['Title'].drop_duplicates()

data['Cleaned_Ingredients'].astype(str)
data['Cleaned_Ingredients'] = data['Cleaned_Ingredients'].apply(
    lambda s: s.translate(str.maketrans('', '', '([$\'_&+,:;=?@\[\]#|<>.^*()%\\!"-])' + U'\xa8')))
data['Cleaned_Ingredients'] = data['Cleaned_Ingredients'].apply(lambda s: s.lower())
data['Cleaned_Ingredients'] = data['Cleaned_Ingredients'].drop_duplicates()

data.to_json('resource/Food_ingredients.json', indent=1, orient='records')

print(len(data))
print(len(data['Title']))  # Title
print(len(data['Cleaned_Ingredients']))  # Ingredient

tfidf = TfidfVectorizer()

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0808601871",
    database='foodrecipe'
)


def Searching_mark(query):
    title = []
    recipe = []
    cursor = db.cursor()
    sequence = []
    words = query.split()
    index = 0
    for i in words:
        sequence.append(spell.correction(i))
        index += 1
    sentence = ' '.join(sequence)

    sql = '''
       SELECT title FROM fav_recipe;
       '''
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        val = json.dumps(i)
        title.append(val.translate(str.maketrans('', '', '([$\'_&+\n?@\[\]#|<>^*()%\\!"-\r\])' + U'\xa8')))

    sql2 = '''
           SELECT recipe FROM fav_recipe;
           '''
    cursor.execute(sql2)
    result2 = cursor.fetchall()
    for i in result2:
        val = json.dumps(i)
        recipe.append(val.translate(str.maketrans('', '', '([$\'_&+\n?@\[\]#|<>^*()%\\!"-\r\])' + U'\xa8')))

    d = {'Title': title, 'Recipe': recipe}
    df = pd.DataFrame(d)
    df = df.drop_duplicates()
    vector = tfidf.fit_transform(df['Title'].astype('U'))
    query_vec = tfidf.transform([sentence])
    results = cosine_similarity(vector, query_vec).reshape((-1,))
    output = []
    for i in results.argsort()[-2:][::-1]:
        output.append(
            {"Title": df.iloc[i, 0],
             "Recipe": df.iloc[i, 1]
             }
        )
    print(output)
    return output


def Getmark_data(userid):
    print('userid: ' + str(userid))
    print(type(userid))
    fav_id = []
    title = []
    recipe = []
    id_mark = []
    image = []
    cursor = db.cursor()
    sql_getmark = '''
        SELECT middle.id_fav_recipe  FROM
        user as person
        left join user_with_fav as middle
        on person.idUser = middle.id_user
        where person.idUser = %s;
        '''
    cursor.execute(sql_getmark, (userid,))
    result_fav_id = cursor.fetchall()
    print('id of user' + str(result_fav_id))
    for i in result_fav_id:
        val = json.dumps(i)
        fav_id.append(val.translate(str.maketrans('', '', '([$\'_&+\n?@\[\]#|<>^*()%\\!"-\r\])' + U'\xa8')))
    for i in fav_id:
        sql = '''
        SELECT title  FROM fav_recipe
        where id_fav_recipe = %s;
        '''
        cursor.execute(sql, (i,))
        result = cursor.fetchall()
        for j in result:
            val = json.dumps(j)
            title.append(val.translate(str.maketrans('', '', '([$\'_&+\n?@\[\]#|<>^*()%\\!"-\r\])' + U'\xa8')))
        sql2 = '''
            SELECT recipe FROM fav_recipe
            where id_fav_recipe = %s;
            '''
        cursor.execute(sql2, (i,))
        result2 = cursor.fetchall()
        for j in result2:
            val = json.dumps(j)
            recipe.append(val.translate(str.maketrans('', '', '([$\'_&+\n?@\[\]#|<>^*()%\\!"-\r\])' + U'\xa8')))

        sql3 = '''
           SELECT id_fav_recipe FROM fav_recipe
           where id_fav_recipe = %s;
           '''
        cursor.execute(sql3, (i,))
        result3 = cursor.fetchall()
        for j in result3:
            val = json.dumps(j)
            id_mark.append(val.translate(str.maketrans('', '', '([$\'_&+\n?@\[\]#|<>^*()%\\!"-\r\])' + U'\xa8')))

        sql4 = '''
            SELECT image FROM fav_recipe
            where id_fav_recipe = %s;
            '''
        cursor.execute(sql4, (i,))
        result4 = cursor.fetchall()
        for j in result4:
            val = json.dumps(j)
            image.append(val.translate(str.maketrans('', '', '([$\'_&+\n?@\[\]#|<>^*()%\\!"\r\])' + U'\xa8')))

    d = {'id_mark': id_mark, 'Title': title, 'Recipe': recipe, 'Image': image}
    df = pd.DataFrame(d)
    df = df.drop_duplicates(subset=['Title'])
    json_result = df.to_json(orient="records")
    output = json.loads(json_result)

    return output


def SearchingByTitle(query):
    sequence = []
    words = query.split()
    index = 0
    for i in words:
        sequence.append(spell.correction(i))
        index += 1
    sentence = ' '.join(sequence)
    Title_vector = tfidf.fit_transform(data['Title'].astype('U'))
    query_vec = tfidf.transform([sentence])
    results = cosine_similarity(Title_vector, query_vec).reshape((-1,))
    output = []
    for i in results.argsort()[-20:][::-1]:
        if results[i] >= 0.1:
            print(results[i])
            print(data.iloc[i, 4])
            print(data.iloc[i, 1])
            print(data.iloc[i, 3])
            print()
            image = data.iloc[i, 4] + str('.jpg')
            output.append(
                {"Title": data.iloc[i, 1],
                 "Recipe": data.iloc[i, 3].translate(
                     str.maketrans('', '', '([$\'_&+\n?@\[\]#|<>^*()%\\!"-\r\])' + U'\xa8')),
                 "Ingredients": data.iloc[i, 2].translate(
                     str.maketrans('', '', '([$\'_&+\n?@\[\]#|<>^*()%\\!"-\r\])' + U'\xa8')),
                 "Image": image
                 }
            )
    return output


def SearchingByIngredients(query):
    sequence = []
    words = query.split()
    index = 0
    for i in words:
        sequence.append(spell.correction(i))
        index += 1
    sentence = ' '.join(sequence)
    Ingredients_vector = tfidf.fit_transform(data['Cleaned_Ingredients'].astype('U'))
    query_vec = tfidf.transform([sentence])
    results = cosine_similarity(Ingredients_vector, query_vec).reshape((-1,))
    output = []
    for i in results.argsort()[-20:][::-1]:
        if results[i] >= 0.1:
            print(results[i])
            print(data.iloc[i, 4])
            print(data.iloc[i, 1])
            print(data.iloc[i, 3])
            print()
            image = data.iloc[i, 4] + str('.jpg')
            output.append(
                {"Title": data.iloc[i, 1],
                 "Recipe": data.iloc[i, 3].translate(
                     str.maketrans('', '', '([$\'_&+\n?@\[\]#|<>^*()%\\!"-\r\])' + U'\xa8')),
                 "Ingredients": data.iloc[i, 2].translate(
                     str.maketrans('', '', '([$\'_&+\n?@\[\]#|<>^*()%\\!"-\r\])' + U'\xa8')),
                 "Image": image
                 }
            )
    return output


def Login_user(username, password):
    array_user = []
    output = []
    cursor = db.cursor()
    sql = '''
        SELECT idUser FROM foodrecipe.user
        where username = %s;
        '''
    val = (username,)
    cursor.execute(sql, val)
    result = cursor.fetchall()
    for i in result:
        val = json.dumps(i)
        array_user.append(val.translate(str.maketrans('', '', '([$\'_&+\n?@\[\]#|<>^*()%\\!"\r\])' + U'\xa8')))

    if username == 'kong' and password == '1234':
        check = True
        output.append(
            {
                'userid': array_user[len(array_user) - 1],
                'user': username,
                'password': password,
                'check': check
            }
        )
        return output
    elif username == 'fax' and password == '1234':
        check = True
        output.append(
            {
                'userid': array_user[len(array_user) - 1],
                'user': username,
                'password': password,
                'check': check
            }
        )
        return output
    elif username == 'plook' and password == '1234':
        check = True
        output.append(
            {
                'userid': array_user[len(array_user) - 1],
                'user': username,
                'password': password,
                'check': check
            }
        )
        return output
    else:
        check = False
        output.append(
            {
                'userid': '',
                'user': username,
                'password': password,
                'check': check
            }
        )
        return output

# if __name__ == '__main__':
# SearchingByTitle("Miso-Butter Roast Chicken With Acorn Squash Panzanella")
# SearchingByIngredients("porkk becauss paek")
