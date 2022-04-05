from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from services.text_tokenizer import text_tokenizer
import pandas as pd
import numpy as np


dataset = pd.read_csv('./data/True.csv', usecols=['title', 'text'])
sample = dataset['title'][:10]

vectorizer = CountVectorizer(tokenizer=text_tokenizer)
# vectorizer = TfidfVectorizer(tokenizer=text_tokenizer)

X_transform_sample = vectorizer.fit_transform(sample)
print(vectorizer.get_feature_names_out())
titles = (vectorizer.get_feature_names_out())
array = X_transform_sample.toarray()

"""
Display top 10 tokens
"""

column_sum = np.sum(array, axis=0)
max_val = np.argpartition(column_sum, -10)[-10:]
top_10 = column_sum[max_val]
print(top_10)
print(titles[np.argpartition(column_sum, -10)[-10:]])
