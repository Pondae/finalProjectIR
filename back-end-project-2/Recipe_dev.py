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
    correc_title = []
    correc_recipe = []
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
        title.append(val)

    sql2 = '''
           SELECT recipe FROM fav_recipe;
           '''
    cursor.execute(sql2)
    result2 = cursor.fetchall()
    for i in result2:
        val = json.dumps(i)
        recipe.append(val)

    for i in title:
        correc_title.append(i.translate(str.maketrans('', '', '([$\'_&+\n?@\[\]#|<>^*()%\\!"-\r\])' + U'\xa8')))
    for i in recipe:
        correc_recipe.append(i.translate(str.maketrans('', '', '([$\'_&+\n?@\[\]#|<>^*()%\\!"-\r\])' + U'\xa8')))

    d = {'Title': correc_title, 'Recipe': correc_recipe}
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


def Getmark_data():
    title = []
    recipe = []
    id = []
    correct_id = []
    correc_title = []
    correc_recipe = []
    cursor = db.cursor()
    sql = '''
    SELECT title  FROM fav_recipe;
    '''
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        val = json.dumps(i)
        title.append(val)

    sql2 = '''
        SELECT recipe FROM fav_recipe;
        '''
    cursor.execute(sql2)
    result2 = cursor.fetchall()
    for i in result2:
        val = json.dumps(i)
        recipe.append(val)

    sql3 = '''
       SELECT id_fav_recipe FROM fav_recipe;
       '''
    cursor.execute(sql3)
    result3 = cursor.fetchall()
    for i in result3:
        val = json.dumps(i)
        id.append(val)

    for i in id:
        correct_id.append(i.translate(str.maketrans('', '', '([$\'_&+\n?@\[\]#|<>^*()%\\!"-\r\])' + U'\xa8')))
    for i in title:
        correc_title.append(i.translate(str.maketrans('', '', '([$\'_&+\n?@\[\]#|<>^*()%\\!"-\r\])' + U'\xa8')))
    for i in recipe:
        correc_recipe.append(i.translate(str.maketrans('', '', '([$\'_&+\n?@\[\]#|<>^*()%\\!"-\r\])' + U'\xa8')))

    d = {'id': correct_id, 'Title': correc_title, 'Recipe': correc_recipe}
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
    for i in results.argsort()[-3:][::-1]:
        image = data.iloc[i, 4] + str('.jpg')
        output.append(
            {"Title": data.iloc[i, 1],
             "Recipe": data.iloc[i, 3].translate(
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
    for i in results.argsort()[-3:][::-1]:
        image = data.iloc[i, 4] + str('.jpg')
        output.append(
            {"Title": data.iloc[i, 1],
             "Recipe": data.iloc[i, 3].translate(
                 str.maketrans('', '', '([$\'_&+\n?@\[\]#|<>^*()%\\!"-\r\])' + U'\xa8')),
             "Image": image
             }
        )
    return output


def Login_user(username, password):
    output = []
    if username == 'kong' and password == 'kong1234':
        check = True
        output.append(
            {
                'user': username,
                'password': password,
                'check': check
            }
        )
        return output
    elif username == 'fax' and password == 'fax1234':
        check = True
        output.append(
            {
                'user': username,
                'password': password,
                'check': check
            }
        )
        return output
    elif username == 'plook' and password == 'plook1234':
        check = True
        output.append(
            {
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
                'user': username,
                'password': password,
                'check': check
            }
        )
        return output

# if __name__ == '__main__':
# SearchingByTitle("Miso-Butter Roast Chicken With Acorn Squash Panzanella")
# SearchingByIngredients("porkk becauss paek")
