import re


def delete_punctuation_marks(text) -> str:
    result = re.sub('[,;.]', '', text)
    return result
