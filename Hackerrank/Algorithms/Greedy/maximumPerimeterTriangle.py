#!/bin/python3

import sys

def maximumPerimeterTriangle(l):
    # Complete this function
    degenerates = []
    l = sorted(l)
    for i in range(len(l)-2):
        
        a = l[i]
        b = l[i + 1]
        c = l[i + 2]
        if a+b>c and a+c>b and b+c>a:
            degenerates.append((a,b,c))
    if len(degenerates) == 0:
        return [-1]
    else:
        sum = 0
        max_perimeter = None
        for i in range(len(degenerates)):
            a,b,c = degenerates[i]
            if sum<a+b+c:
                sum = a+b+c
                max_perimeter = [a,b,c]
        return max_perimeter
if __name__ == "__main__":
    n = int(input().strip())
    l = list(map(int, input().strip().split(' ')))
    result = maximumPerimeterTriangle(l)
    print (" ".join(map(str, result)))