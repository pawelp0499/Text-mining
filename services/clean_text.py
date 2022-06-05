import re


def clean_text(text: str) -> str:
    text_low = text.lower()
    text_without_emoticons = re.sub(r'[:|;][-]?[)|(<>][_@]', '', text_low)
    text_without_number = re.sub(r'\d', '', text_without_emoticons)
    text_without_html = re.sub(r'<.*?>', '', text_without_number)
    text_without_https = re.sub(r'http[s]?://\S+', '', text_without_html)
    text_without_punc_marks = re.sub(r'\W(?<!\s)', '', text_without_https)
    result = text_without_punc_marks.strip()
    return result
