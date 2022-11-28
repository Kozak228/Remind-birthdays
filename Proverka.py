from os import path

def proverka_file(file_name, path_file = ""):
    if path_file == "":
        full_path = path.abspath(__file__)
        full_path_file = full_path[:full_path.rindex('\\') + 1]
        full_path_file = f"{full_path}{file_name}.json"
    else:
        full_path_file = f"{path_file}{file_name}.json"

    return True if path.isfile(full_path_file) else False

def proverka_dir(path_dir):
    if path_dir != "":
        path_dir += "\\"
    else:
        path_dir = path.abspath(__file__)
        path_dir = path_dir[:path_dir.rindex("\\") + 1]

    return path_dir