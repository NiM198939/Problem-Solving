#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum_pairs = 0
    decent_number = ''
    i = 3
    j = 5
    counter = 0
    ans = None
    mul5 = 1
    while mul5>0:
        mul5 = int(n/3)*i - i*counter
        mod5 = n%3 + i*counter
        if mod5%5 == 0:
            if mul5+mod5 == n:
                ans = '5'*mul5+'3'*mod5
                break
        counter = counter + 1
    if ans:
        print(ans)
    else:
        print(-1)
        
            