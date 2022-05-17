from nltk import PorterStemmer, word_tokenize


def stemmer(sentence):
    porter = PorterStemmer()
    t_words = word_tokenize(sentence)
    stem_sentence = []
    for word in t_words:
        stem_sentence.append(porter.stem(word))
    return stem_sentence
