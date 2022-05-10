from nltk.stem.porter import *
from nltk import word_tokenize


def stemmer(text: str) -> list:
    ps = PorterStemmer()

    words = word_tokenize(text)
    stem = []
    for w in words:
        stem.append(ps.stem(w))
    return stem
