#!/bin/python3

import sys

def super_reduced_string(s):
    # Complete this function
    a = s[0]
    count = 0
    ans = ''
    
    for i in range(len(s)):
        if a != s[i]:
            mod = count%2
            if count==0 or mod != 0:
                ans = ans + a
            a = s[i]
            count = 1
        else:
            count = count + 1
    mod = count%2
    if count==0 or mod != 0:
        ans = ans + a
    if len(s) == len(ans):
        return s
    if ans =='':
        return 'Empty String'
    else:
        return super_reduced_string(ans)
            
s = input().strip()
result = super_reduced_string(s)
print(result)
