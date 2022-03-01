import re


def delete_html(text) -> str:
    result = re.sub('<.*?>', '', text)
    return result
