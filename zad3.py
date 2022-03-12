from nltk.stem.porter import *


def stemmer(text: str) -> list:
    ps = PorterStemmer()
    lala = list(text.split(" "))

    for w in lala:
        print(ps.stem(w))
