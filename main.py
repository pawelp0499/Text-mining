from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from services.text_tokenizer import text_tokenizer
import pandas as pd


dataset = pd.read_csv('./data/True.csv', usecols=['title', 'text'])
sample = dataset['title'].sample(10)

vectorizer = CountVectorizer(tokenizer=text_tokenizer)
# vectorizer = TfidfVectorizer(tokenizer=text_tokenizer)

x_transform_sample = vectorizer.fit_transform(sample)
print(x_transform_sample.toarray())
