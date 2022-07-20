#!/usr/bin/python3

"""
Module contains the definition of "save_to_json_file" function


"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'
try:
    myList = load_from_json_file(filename)
except FileNotFoundError:
    myList = []

inputList = []
if len(sys.argv) > 1:
    inputList = sys.argv[1:]

myList.extend(inputList)
save_to_json_file(myList, filename)
