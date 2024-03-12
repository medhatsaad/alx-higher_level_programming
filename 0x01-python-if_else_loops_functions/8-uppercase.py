#!/usr/bin/pyhon3
def uppercase(str):
    for i in str:
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            print({}.format(chr(ord(str[i]) + 32)))
        else:
            print({}.format(str[i]))
