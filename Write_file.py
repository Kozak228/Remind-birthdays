from json import dumps

from Sorted import sort_dict

def write_file(dicts, file_name, file_path):
    dicts = sort_dict(dicts)
    
    j = dumps(dicts)

    with open(f'{file_path}{file_name}.json', 'w') as f:
        f.write(j)

    f.close()