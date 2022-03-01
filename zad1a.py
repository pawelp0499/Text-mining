import re


"""Function to remove numbers from text"""


def delete_numbers(text: str) -> str:
    """Enter a text as a string parameter and get it
     without any unwanted characters"""
    result = re.sub('\d', '', text)
    return result
