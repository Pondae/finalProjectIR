import json
import string
import mysql.connector
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# pip install mysql-connector
import pandas as pd

data = pd.read_csv('resource/Food_ingredients.csv')
data.drop_duplicates()

data['Title'] = data['Title'].astype(str)
data['Title'] = data['Title'].apply(lambda s: s.translate(str.maketrans('', '', '([$\'_&+,:;=?@\[\]#|<>.^*()%\\!"-])' +U'\xa8')))
data['Title'] = data['Title'].apply(lambda s: s.lower())
data['Title'] = data['Title'].drop_duplicates()

data['Cleaned_Ingredients'].astype(str)
data['Cleaned_Ingredients'] = data['Cleaned_Ingredients'].apply(
    lambda s: s.translate(str.maketrans('', '', string.punctuation + u'\xa0')))
data['Cleaned_Ingredients'] = data['Cleaned_Ingredients'].apply(lambda s: s.lower())
data['Cleaned_Ingredients'] = data['Cleaned_Ingredients'].drop_duplicates()

data.to_json('resource/Food_ingredients.json', indent=1, orient='records')


# print(len(data))
# print(len(data['Title']))  # Title
# print(len(data['Cleaned_Ingredients']))  # Ingredient

tfidf = TfidfVectorizer()


def SearchingByTitle(query):
    Title_vector = tfidf.fit_transform(data['Title'].astype('U'))
    query_vec = tfidf.transform([query])
    results = cosine_similarity(Title_vector, query_vec).reshape((-1,))
    output = []
    for i in results.argsort()[-3:][::-1]:
        output.append(
            {"Title": data.iloc[i, 1], "Recipe": data.iloc[i, 3]
             }
        )
    return output


def SearchingByIngredients(query):
    Ingredients_vector = tfidf.fit_transform(data['Cleaned_Ingredients'].astype('U'))
    query_vec = tfidf.transform([query])
    results = cosine_similarity(Ingredients_vector, query_vec).reshape((-1,))
    output = []
    for i in results.argsort()[-3:][::-1]:
        output.append(
            {"Title": data.iloc[i, 1], "Recipe": data.iloc[i, 3]
             }
        )
    return output


def Loginuser(username, password):
    if username == 'peter' and password == 'honey':
        return True
    else:
        return False


# if __name__ == '__main__':
    # SearchingByTitle("Miso-Butter Roast Chicken With Acorn Squash Panzanella")
