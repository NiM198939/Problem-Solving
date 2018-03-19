#!/bin/python3

import sys

def toys(w):
    # Complete this function
    w = sorted(w)
    b = w[0] + 4
    c = 1
    for i in range(len(w)):
        if w[i]<=b:
            continue
        else:
            c = c + 1
            b = w[i] + 4
    return c        
        
if __name__ == "__main__":
    n = int(input().strip())
    w = list(map(int, input().strip().split(' ')))
    result = toys(w)
    print(result)
