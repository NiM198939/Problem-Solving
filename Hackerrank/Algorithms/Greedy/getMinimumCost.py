#!/bin/python3

import sys
import math
def getMinimumCost(n, k, c):
    # Complete this function
    c = sorted(c, reverse=True)
    minCost = 0 
    for i in range(n):
        minCost = minCost + (math.floor(i/k)+1)*c[i]
    return minCost
        
n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
c = list(map(int, input().strip().split(' ')))
minimumCost = getMinimumCost(n, k, c)
print(minimumCost)