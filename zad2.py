import re


"""Function to remove #hashtags from text"""


def delete_hashtags(text: str) -> str:
    """Enter a text as a string parameter and get it
         without any unwanted characters"""
    result = re.sub("#[^\s]+", '', text)
    return result
