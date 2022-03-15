def read_file(path: str):
    f = open(path, encoding='UTF-8')
    data = f.read().splitlines()
    f.close()
    return data
