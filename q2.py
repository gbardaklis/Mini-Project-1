#/////////////////////   IMPORTS   /////////////////////

import pandas as pd 
import numpy as np 
from sklearn.feature_extraction.text import CountVectorizer

#/////////////////////   Q2   /////////////////////

df = pd.read_json(r'goemotions.json\goemotions.json')
df.to_csv(r'C:\Users\DanWB\OneDrive\Documents\CONU\COMP472\Mini-Project-1\test.txt', index = False)

f = open("test.txt", "r")

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(f)
print(X.toarray())