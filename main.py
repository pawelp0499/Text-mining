import pandas as pd
from services.clear_text import clear_text
from services.text_tokenizer import *
draw_wordcloud, text_tokenizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import numpy as np


def main(name):
    true_posts = pd.read_csv('./data/True.csv', usecols=['title', 'text'])
    fake_posts = pd.read_csv('./data/Fake.csv', usecols=['title', 'text'])

    entire_text = ' '.join(true_posts['title'].to_list())
    clear_text = clear_text(entire_text)
    tokens = text_tokenizer(clear_text)

    vectorizer = TfidfVectorizer(tokenizer=text_tokenizer)
    X_transform = vectorizer.fit_transform(true_posts['title'])
    print(np.asarray(X_transform)[0])

    #uniques = list(set(tokens))
    #bow = {unique: tokens.count(unique) for unique in uniques}
    #draw_wordcloud(bow, 'word cloud')


if __name__ == '__main__':
    main('PyCharm')


