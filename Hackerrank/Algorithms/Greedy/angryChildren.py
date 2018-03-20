#!/bin/python3

import sys

def angryChildren(k, arr):
    # Complete this function
    arr = sorted(arr)
    remain = len(arr) - k 
    if remain == 0 :
        return arr[len(arr)-1] - arr[0]
    else:
        minium = sys.maxsize
        for i in range(len(arr)-k):
            value = arr[i+k-1] - arr[i]
            if value < minium:
                minium = value
        return  minium
    
if __name__ == "__main__":
    n = int(input().strip())
    k = int(input().strip())
    arr = []
    arr_i = 0
    for arr_i in range(n):
       arr_t = int(input().strip())
       arr.append(arr_t)
    result = angryChildren(k, arr)
    print(result)
