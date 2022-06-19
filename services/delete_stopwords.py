from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def stopwords_del(text: str):
    stop_words = stopwords.words("english")
    word_token = word_tokenize(text)
    return [w for w in word_token if not w.lower() in stop_words]


def stopwords_del_tok(text: str):
    stop_words = stopwords.words("english")
    return [w for w in text if not w.lower() in stop_words]
