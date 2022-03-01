import re


"""Function to remove some punctuation marks from text"""


def delete_punctuation_marks(text: str) -> str:
    """Enter a text as a string parameter and get it
         without any unwanted characters"""
    result = re.sub('[,;.]', '', text)
    return result
