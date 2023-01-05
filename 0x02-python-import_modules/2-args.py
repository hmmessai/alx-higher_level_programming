#!/usr/bin/python3
import sys
count = 1
argv = sys.argv
arg_num = len(argv)

print("{} argument{}{}".format(arg_num - 1,"" if arg_num == 2 else "s" , "." if arg_num == 1 else ":"))
for i in range(arg_num - 1):
    print("{}: {}".format(count, argv[count]))
    count += 1
