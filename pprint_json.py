#!/usr/bin/python3
# -*- coding=utf-8 -*-
import json
import codecs
import pprint


def load_data(filepath):
    fileObj = codecs.open(filepath, "r", "utf_8_sig")
    json_data = fileObj.read()
    data = json.loads(json_data)
    return (data)


def pretty_print_json(data):
    pprint.pprint(data)

if __name__ == '__main__':
    N = input('введите путь к файлу : ')
    pprint.pprint(load_data(N))
