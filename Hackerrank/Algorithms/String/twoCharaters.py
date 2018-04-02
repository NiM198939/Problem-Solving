#!/bin/python

import sys

def twoCharaters(s):
    # Complete this function
    length =  0 
    unique_chars =list(set(s))
    for i in range(len(unique_chars)):
        for j in range(i+1,len(unique_chars)):
            s1 = [c for c in s if c==unique_chars[i] or c==unique_chars[j]]
            consecutive = True
            for k in range(len(s1)-1):
                if s1[k] == s1[k+1]:
                    consecutive = False
                    break
            if consecutive:
                length = max(length,len(s1))
            
    return length
            
if __name__ == "__main__":
    l = int(input().strip())
    s = input().strip()
    result = twoCharaters(s)
    print(result)
