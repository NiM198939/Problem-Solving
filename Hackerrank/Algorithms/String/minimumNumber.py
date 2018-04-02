#!/bin/python

import sys

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    check1,check2,check3,check4 = False,False,False,False
    for i in range(len(password)):
        if not check1 and ord(password[i]) <=90 and ord(password[i])>=65:
            check1 = True
        if not check2 and ord(password[i]) <=122 and ord(password[i])>=97:
            check2 = True
        if not check3 and password[i] in ('!','@','#','$','%','&','*','(',')','-','+'):
            check3 = True
        if not check4 and ord(password[i]) <=57 and ord(password[i])>=48:
            check4 = True
    count = 4 -(check1+check2+check3+check4)
    if n < 6:
        case = 6 -n
        if case<count:
            return count
        else:
            return count+(case-count)
        
    if n>=6:
        return count
            

if __name__ == "__main__":
    n = int(raw_input().strip())
    password = raw_input().strip()
    answer = minimumNumber(n, password)
    print answer
