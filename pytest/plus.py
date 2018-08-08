#!/bin/env python3

def trim(s):
    n = len(s)
    while n > 0:
        if s[0] == ' ' and s[-1] == ' ':
            s = s[1:len(s) - 1]
            n = n - 2
        elif s[0] == ' ':
            s = s[1:]
            n = n - 1
        elif s[-1] == ' ':
            s = s[:-1]
            n = n - 1
        else:
            return s
    return s
x=input(">>>>>")
y = trim(x)
print(y)
print(len(y))



z=x.strip()
print(z)

	
