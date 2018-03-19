#!/bin/python3

import sys

def minimumAbsoluteDifference(n, arr):
    # Complete this function
    arr = sorted(arr)
    minimum = min(abs(x-y) for x,y in zip(arr,arr[1:]))
    return minimum

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = minimumAbsoluteDifference(n, arr)
    print(result)
