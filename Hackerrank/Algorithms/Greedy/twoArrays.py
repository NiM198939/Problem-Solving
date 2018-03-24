#!/bin/python3

import sys

def twoArrays(k, A, B):
    # Complete this function
    A = sorted(A)
    B = sorted(B,reverse=True)
    ans = 'YES'
    for i in range(len(A)):
        if A[i]+B[i] < k:
            ans = 'NO'
            break
    return ans

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        A = list(map(int, input().strip().split(' ')))
        B = list(map(int, input().strip().split(' ')))
        result = twoArrays(k, A, B)
        print(result)
