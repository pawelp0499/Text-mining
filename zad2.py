import re


"""Function to show hashtags from text"""


def extract_hashtags(text: str):
    """Enter a text as a string parameter and get
        the result as extracted hashtags"""
    result = re.findall("#[^\s]+", text)
    for hashtag in result:
        print(hashtag)

