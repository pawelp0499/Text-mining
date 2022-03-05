import re


"""Function to show some selected emoticons from text"""


def extract_emoticons(text: str):
    """Enter a text as a string parameter and get
        the result as extracted emoticons"""
    result = re.findall(r"[:;][)\-(<>]+", text)
    for emoticon in result:
        print(emoticon)
