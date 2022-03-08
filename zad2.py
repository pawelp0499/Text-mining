import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')


def remove_stop_words(text: str) -> str:
    all_stopwords = stopwords.words('english')

    text_tokens = word_tokenize(text)
    tokens_without_sw = [word for word in text_tokens if
                         not word in all_stopwords]
    return tokens_without_sw
