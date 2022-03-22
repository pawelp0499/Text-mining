import pandas as pd
from services.clear_text import clear_text


def read_file(path: str, col: str) -> list:
    data = pd.read_csv(path, usecols=[col], encoding='UTF-8')
    data = data.values.astype(str)

    cleared_data = []
    for row in data:
        cleared_data.append(clear_text(str(row)))
    return cleared_data
