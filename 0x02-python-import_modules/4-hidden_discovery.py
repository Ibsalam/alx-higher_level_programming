#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    functions = dir()
    for filtered in range(0, len(functions)):
        if functions[filtered][:2] != "__":
            print("(:s)".format(functions[filtered]))
