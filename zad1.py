import re


def clear_text(text: str) -> str:
    emoticons = re.sub(r"[],[']", '', str(re.findall(r"[:;][)\-(<>]+", text)))
    text_without_emoticons = re.sub(r"[:;][)\-(<>]+", '', text.lower())
    no_digits = re.sub(r'\d', '', text_without_emoticons)
    no_html_tags = re.sub('<.*?>', '', no_digits)
    no_punctuation_marks = re.sub('[,;.]', '', no_html_tags)
    no_multiple_spaces = re.sub(' +', ' ', no_punctuation_marks)
    result = no_multiple_spaces + emoticons
    return result
