from services.clear_text import clear_text
from services.stem_text import stemmer
from services.delete_stopwords import stopwords_del


def text_tokenizer(text: str) -> list:
    cleaned = clear_text(text)
    stopw = stopwords_del(cleaned)
    stemmed = stemmer(stopw)
    word_list = []
    for word in stemmed:
        if len(word) > 3:
            word_list.append(word)
    return word_list
