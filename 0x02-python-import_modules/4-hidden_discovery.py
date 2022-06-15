#!/usr/bin/python3
if __name__ == "__main__":
    """Print names defined by a module"""
    import hidden_4
for str in dir(hidden_4):
    if "__" not in str:
        print(str)
