#!/usr/bin/python3
def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False


def uppercase(string):
    for c in string:
        print("{:c}"
              .format(ord(c) if not islower(c) else ord(c) - 32),
              end="")
    print("")
