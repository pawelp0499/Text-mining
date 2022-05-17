from sklearn.metrics.pairwise import euclidean_distances, cosine_distances,\
    cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from services.text_tokenizer import text_tokenizer
import pandas as pd


data = pd.read_csv('./data/dataset.csv')
print(data)

vectorizer = CountVectorizer(tokenizer=text_tokenizer)

X_transform = vectorizer.fit_transform(data['TeamName'])
array = X_transform.toarray()

df = pd.DataFrame(array, columns=vectorizer.get_feature_names_out())

print(f"Euclidean distance:\n {euclidean_distances(df,df)}")
print(f"Cosine distance:\n {cosine_distances(df,df)}")
print(f"Cosine similarity:\n {cosine_similarity(df,df)}")
