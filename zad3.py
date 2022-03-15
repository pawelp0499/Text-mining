from nltk.stem.porter import *


def stemmer(text: str) -> list:
    ps = PorterStemmer()
    str_as_list = list(text.split(" "))

    stem = []
    for w in str_as_list:
        stem.append(ps.stem(w))
    return stem
