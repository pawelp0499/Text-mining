import re


"""Function to remove some emoticons from text"""


def delete_emoticons(text: str) -> str:
    """Enter a text as a string parameter and get it
         without any unwanted characters"""
    result = re.sub("[:;][)\-(<>]+", '', text)
    return result
