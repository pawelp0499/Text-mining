from services.clean_text import clean_text
from services.stem_text import stemmer
from services.delete_stopwords import stopwords_del_tok
from nltk.tokenize import word_tokenize


def text_tokenizer(text: str):
    cleaned = clean_text(text)
    tokens = word_tokenize(cleaned)
    without_stopwords = stopwords_del_tok(tokens)

    return [stemmer(w) for w in without_stopwords if len(w) > 3]
