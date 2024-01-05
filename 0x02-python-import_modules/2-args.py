#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_args = len(sys.argv) - 1
if num_args == 0:
    print("0 argument(s):")
    print(".")
else:
    print(f"{num_args} {'argument' if num_args == 1 else 'arguments'}:")
    
    for i in range(1, num_args + 1):
        print(f"{i}: {sys.argv[i]}")
