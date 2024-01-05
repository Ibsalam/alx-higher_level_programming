#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arguments = 0
    for arg in range(1, len(argv)):
        arguments += int(argv[arg])
    print("{}".format(arguments))
