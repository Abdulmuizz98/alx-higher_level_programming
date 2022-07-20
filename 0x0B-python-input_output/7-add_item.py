#!/usr/bin/python3

"""
contains a script


"""
if __name__ == "__main__":
    """ Script that adds all arguments to a Python list,
        and then save them to a file
    """
    import sys
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json = __import__('6-load_from_json_file').load_from_json_file

    filename = 'add_item.json'
    try:
        myList = load_from_json(filename)
    except FileNotFoundError:
        myList = []

    inputList = []
    if len(sys.argv) > 1:
        inputList = sys.argv[1:]

    myList.extend(inputList)
    save_to_json_file(myList, filename)
