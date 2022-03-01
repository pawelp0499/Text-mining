import re


"""Function to remove HTML tags from text"""


def delete_html(text: str) -> str:
    """Enter a text as a string parameter and get it
         without any unwanted characters"""
    result = re.sub('<.*?>', '', text)
    return result
