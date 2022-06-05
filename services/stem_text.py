from nltk import PorterStemmer


def stemmer(word: str) -> str:
    ps = PorterStemmer()
    return ps.stem(word)
    
    
def stemming_list(words_without_stopwords: str) -> list:
    ps = PorterStemmer()
    stem_list = []
    for word in words_without_stopwords:
        stem_list.append(ps.stem(word))
    return stem_list
