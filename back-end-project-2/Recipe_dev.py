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
data['Title'] = data['Title'].apply(
    lambda s: s.translate(str.maketrans('', '', string.punctuation + u'\xa0')))
data['Title'] = data['Title'].apply(lambda s: s.lower())
data['Title'] = data['Title'].drop_duplicates()

data['Cleaned_Ingredients'].astype(str)
data['Cleaned_Ingredients'] = data['Cleaned_Ingredients'].apply(
    lambda s: s.translate(str.maketrans('', '', string.punctuation + u'\xa0')))
data['Cleaned_Ingredients'] = data['Cleaned_Ingredients'].apply(lambda s: s.lower())
data['Cleaned_Ingredients'] = data['Cleaned_Ingredients'].drop_duplicates()

# print(len(data))
# print(len(data['Title']))  # Title
# print(len(data['Cleaned_Ingredients']))  # Ingredient

tfidf_Title_vector = TfidfVectorizer()
tfidf_Ingredients_vector = TfidfVectorizer()
Title_vector = tfidf_Title_vector.fit_transform(data['Title'].astype('U'))
Ingredients_vector = tfidf_Ingredients_vector.fit_transform(data['Cleaned_Ingredients'].astype('U'))


def SearchingByTitle(query):
    query_vec = tfidf_Title_vector.transform([query])
    results = cosine_similarity(Title_vector, query_vec).reshape((-1,))
    output = []
    for i in results.argsort()[-10:][::-1]:
        output.append(
            {"Title": data.iloc[i, 0], "Recipe": data.iloc[i, 2]
             }
        )
    return output


def SearchingByIngredients(query):
    query_vec = tfidf_Ingredients_vector.transform([query])
    results = cosine_similarity(Ingredients_vector, query_vec).reshape((-1,))
    output = []
    for i in results.argsort()[-20:][::-1]:
        output.append(
            {"Title": data.iloc[i, 0], "Recipe": data.iloc[i, 2]
             }
        )
    return output


def Loginuser(username, password):
    if username == 'peter' and password == 'honey':
        return True
    else:
        return False
