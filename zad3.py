import re


def delete_emoticons(text) -> str:
    result = re.sub("[:;][)\-(<>]+", '', text)
    return result
