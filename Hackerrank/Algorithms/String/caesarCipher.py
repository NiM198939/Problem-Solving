#!/bin/python3

import sys

def caesarCipher(s, k):
    # Complete this function
    stringalphA = 'abcdefghijklmnopqrstuvwxyz'
    stringalphB = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result =''
    for i in s:
        if i in stringalphA:
            result= result + stringalphA[(stringalphA.index(i)+k)%26]
        elif i in stringalphB:
            result= result + stringalphB[(stringalphB.index(i)+k)%26]
        else:
            result= result + i
    return result

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)