import re


def delete_numbers(text) -> str:
    result = re.sub('\d', '', text)
    return result
