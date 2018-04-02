#!/bin/python

import sys

def camelcase(s):
    # Complete this function
    count = 1
    for i in range(len(s)):
       if ord(s[i]) <=90 and ord(s[i])>=65:
            count = count + 1
    return count
        
if __name__ == "__main__":
    s = raw_input().strip()
    result = camelcase(s)
    print result
