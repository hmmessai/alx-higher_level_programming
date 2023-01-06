#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    sum = 0
    for i in range(len(args) - 1):
        sum += int(args[i + 1])
    print(sum)
