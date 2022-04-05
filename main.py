from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from services.text_tokenizer import text_tokenizer
import pandas as pd
import numpy as np


dataset = pd.read_csv('./data/True.csv', usecols=['title', 'text'])
sample = dataset['title'][:10]

vectorizer = CountVectorizer(tokenizer=text_tokenizer)
vectorizer_tf = TfidfVectorizer(tokenizer=text_tokenizer)

X_transform_sample = vectorizer.fit_transform(sample)
X_transform_sample_tf = vectorizer_tf.fit_transform(sample)
print(vectorizer.get_feature_names_out())
titles = (vectorizer.get_feature_names_out())
array = X_transform_sample.toarray()
array_tf = X_transform_sample_tf.toarray()

"""
Display top 10 tokens
"""

column_sum = np.sum(array, axis=0)
max_val_col = np.argpartition(column_sum, -10)[-10:]
top_10 = column_sum[max_val_col]
print(top_10)
print(titles[np.argpartition(column_sum, -10)[-10:]])

"""
Display top 10 documents
"""

print(array)
row_sum = np.sum(array, axis=1)
max_val_row = np.argpartition(row_sum, -10)[-10:]
top_10_docs = row_sum[max_val_row]
print(top_10_docs)

"""
Display top 10 most important tokens
"""

tf_col_sum = np.sum(array_tf, axis=0)
max_tf_val_col = np.argpartition(tf_col_sum, -10)[-10:]
top_10_tf = tf_col_sum[max_tf_val_col]
print(top_10_tf)
print(titles[np.argpartition(tf_col_sum, -10)[-10:]])
