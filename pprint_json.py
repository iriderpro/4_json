#!/usr/bin/python3
# -*- coding=utf-8 -*-
import json
import codecs
import pprint


def load_data(filepath):
    file_obj = codecs.open(filepath, "r", "utf_8_sig")
    json_data = file_obj.read()
    json_loaded = json.loads(json_data)
    return json_loaded


if __name__ == '__main__':
    n = input('введите путь к файлу : ')
    pprint.pprint(load_data(n))
