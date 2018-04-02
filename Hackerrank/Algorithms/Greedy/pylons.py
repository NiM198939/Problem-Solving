#!/bin/python3

import sys

def pylons(k, arr):
    # Complete this function
    distance = 0
    i = 0
    j = 0
    count = 0
    for l in len(arr):
        if arr[l] == 1:
             if j-i <=k-1:
                 i = j
                 count = count + 1
                 
             else:
                return -1
        j = j + 1
if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = pylons(k, arr)
    print(result)
