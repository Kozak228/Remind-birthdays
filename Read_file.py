from json import loads

def read_file(file_name, file_path):
    with open(f'{file_path}{file_name}.json') as f:
        slovar = loads(f.read())
    return slovar