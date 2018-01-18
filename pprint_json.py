import json
import sys
import os


def load_data(filepath):
    with open(filepath, 'r', encoding='utf8') as file_obj:
        python_obj = json.load(file_obj)
    return python_obj


def prettify_json(py_obj):
    json_str = json.dumps(
        py_obj,
        ensure_ascii=False,
        indent=4,
        sort_keys=True,
    )
    return json_str


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            print (prettify_json(load_data(sys.argv[1])))
        else:
            print('файла не существует')
    else:
        print ('нет входного файла')
