import re


def delete_hashtags(text) -> str:
    result = re.sub("#[^\s]+", '', text)
    return result
