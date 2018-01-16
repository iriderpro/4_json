import json
import sys
import os


def deserialize_fp_json(filepath):
    with open(filepath, "r", encoding='utf8', errors='ignore') as file_obj:
        json_load = json.load(file_obj)
    return json_load


def serialize_obj_json(json_obj):
    json_dumps = json.dumps(json_obj, ensure_ascii=False,
                            indent=4, sort_keys=True)
    return json_dumps


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            print (serialize_obj_json(deserialize_fp_json(sys.argv[1])))
        else:
            print("файла не существует")
    else:
        print ("нет входного файла")
