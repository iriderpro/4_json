import json
import sys
import os


def load_data(filepath):

    with open(filepath, "r", encoding='utf8', errors='ignore') as file_obj:

        json_load = json.load(file_obj)

    print(json.dumps(json_load, ensure_ascii=False, indent=4, sort_keys=True))


if __name__ == '__main__':

    if len(sys.argv) > 1:

        load_data(sys.argv[1])

    else:
        print("нет входного файла")
