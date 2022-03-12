from nltk.stem.porter import *


def stemmer(text: str) -> list:
    ps = PorterStemmer()
    str_as_list = list(text.split(" "))

    for w in str_as_list:
        print(ps.stem(w))
