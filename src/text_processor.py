#!/usr/bin/python
# -*- coding: utf-8 -*-
# Bruno Melo (bjmm@acm.org)
import sqlite3
import nltk
import re
import string

stopwords_pt = nltk.corpus.stopwords.words('portuguese')
stopwords_pt = map(lambda w: unicode(w, 'utf-8'), stopwords_pt)
stopwords_en = nltk.corpus.stopwords.words('english')
stopwords_en = map(lambda w: unicode(w, 'utf-8'), stopwords_en)
dbName = 'twitterData.db'
conn = sqlite3.connect(dbName)
cursor = conn.cursor()

result = cursor.execute('select message from twitterStatus')
ret = result.fetchall()
statuses = [status[0] for status in ret]

exclude = set(string.punctuation)
corpora = []
for st in statuses:
    word_list = map(lambda w:''.join(ch for ch in w if ch not in exclude), re.split('\s+', st.lower()))
    word_list = filter(lambda w: not w.startswith('@'), word_list) # exclude references
    word_list = filter(lambda w: not w.startswith('http'), word_list) # exclude urls
    word_list = filter(lambda w: not w.startswith('rt'), word_list) # exclude urls
    word_list = filter(lambda w: not w.isdigit(), word_list) # exclude numbers
    word_list = filter(lambda w: not w in stopwords_pt, word_list) # exclude stopwords (pt)
    word_list = filter(lambda w: not w in stopwords_en, word_list) # exclude stopwords (en)
    corpora.append(' '.join(word_list))

#print corpora
mytexts = nltk.text.TextCollection(corpora)
print mytexts.idf("python") # idf de 'python' em todo o corpus
print mytexts.idf("nokia") 
print mytexts.idf("filosofia") 
print mytexts.idf("pitomba") 
#print mytexts.tf("palavra", "palavras nos twitters do fulaninho") # tf de 'palavra' em nos textos (todos os twitts) do fulaninho
