import json
import sys
import os


def load_data(filepath):

    with open(filepath, "r", encoding='utf8', errors='ignore') as file_obj:

        json_load = json.load(file_obj)

    return json_load


def pretty_print_json(json_obj):

    json_dumps = json.dumps(json_obj, ensure_ascii=False, indent=4, sort_keys=True)

    return json_dumps


if __name__ == '__main__':

    if len(sys.argv) > 1:

        if os.path.exists(sys.argv[1]):

            print (pretty_print_json(load_data(sys.argv[1])))

        else:
            print("файла не существует")

    else:
        print ("нет входного файла")
