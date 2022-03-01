import nltk
# from bm25 import *
import re

nltk.download('stopwords')
nltk.download('punkt')
import pandas as pd
import string
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from spellchecker import SpellChecker

spell = SpellChecker()

data = pd.read_csv('lyrics.csv')
data['Lyric'] = data['Lyric'].astype(str).apply(
    (lambda s: s.translate(str.maketrans('', '', string.punctuation + u'\xa0'))))
data = data.drop_duplicates()
data['ALink'] = data['ALink'].apply(
    (lambda s: s.translate(str.maketrans('', '', string.punctuation + u'\xa0'))))
data = data[data.Idiom == "ENGLISH"]
data = data.drop_duplicates()
tfidf = TfidfVectorizer(ngram_range=(1, 3))  # ngram_range=(1, 3)
# bm25 = BM25()
tf = CountVectorizer(ngram_range=(1, 3))  # ngram_range=(1, 3)
X = tfidf.fit_transform(data['Lyric'].astype('U'))
Y = tf.fit_transform(data['Lyric'].astype('U'))
# bm25.fit(data["Lyric"].astype('U'))
jsonData = pd.read_json('New_export.json')
dicword = []

inputfile = open('engmix.txt', "r", encoding='utf8')
for line in inputfile:
    line = line.replace("?", " ")
    word = line.strip()
    dicword.append(word)
inputfile.close()


def FixspellSearch(query):
    query = query.lower().split()
    spelling = [spell.correction(word) for word in query]
    misspelledwords = []
    for i in query:
        if i not in dicword:
            x = spell.correction(str(i))
            print(x)
            misspelledwords.append(i)
    return spelling





def searchingTF_IDF(query):
    spell = query
    str1 = ""
    for ele in spell:
        str1 += ele
    query = str1
    query = query.lower()
    query_vec = tfidf.transform([query])
    results = cosine_similarity(X, query_vec).reshape((-1,))
    output = []
    for i in results.argsort()[-10:][::-1]:
        output.append(
            {"artist": data.iloc[i, 0], "Songname": data.iloc[i, 1], "Lyric": data.iloc[i, 3]
             }
        )
    return output


def searchingTF(query):
    query_vec = tf.transform([query])
    results = cosine_similarity(Y, query_vec).reshape((-1,))
    output = []
    for i in results.argsort()[-10:][::-1]:
        output.append(
            {"artist": data.iloc[i, 0], "Songname": data.iloc[i, 1], "Lyric": data.iloc[i, 3]
             }
        )

    return output


def searchingBM25(query):
    result = bm25.transform(query, data[data.Idiom == "ENGLISH"]["Lyric"].astype('U'))
    output = []
    for i in result.argsort()[-10:][::-1]:
        output.append(
            {"artist": data.iloc[i, 0], "Songname": data.iloc[i, 1], "Lyric": data.iloc[i, 3]
             }
        )
    return output


def Matching_check(sentence, keyVal):
    keyVal = keyVal.split()
    correct = any(w in sentence.lower().split(' ') for w in keyVal)
    if correct:
        return True
    else:
        return False


def Input_songname(query):
    data = jsonData
    Correctsong = []
    output = []
    for i in data:
        sentence = data[i]['SName']
        check = Matching_check(sentence, query)
        if check:
            Correctsong.append(i)

    i = Correctsong[0]
    output.append({
        'Lyric': data[i]['Lyric']
    })
    return output


def Input_artist_name(query):
    data = jsonData
    CorrectIndex = []
    wordsort = []
    output = []
    for i in data:
        sentence = data[i]['artist']
        check = Matching_check(sentence, query)
        if check:
            CorrectIndex.append(i)
    for i in CorrectIndex:
        sentence = data[i]['SName']
        wordsort.append(sentence)
    sorted_list = sorted(wordsort)
    for i in sorted_list:
        output.append(
            {'Songname': i}
        )
    return output
