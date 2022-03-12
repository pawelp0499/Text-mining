from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def remove_stop_words(text: str) -> str:
    eng_stopwords = stopwords.words('english')

    token = word_tokenize(text)
    tokens_without_sw = [word for word in token if
                         word not in eng_stopwords]
    return ' '.join([str(i) for i in tokens_without_sw])
