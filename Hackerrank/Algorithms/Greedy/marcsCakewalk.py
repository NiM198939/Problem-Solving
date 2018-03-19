#!/bin/python3

import sys

def marcsCakewalk(calorie):
    # Complete this function
    sum = 0 
    n = 0
    for c in calorie:
        sum = sum + c*pow(2,n)
        n = n + 1
    return sum
    
if __name__ == "__main__":
    n = int(input().strip())
    calorie = sorted(list(map(int, input().strip().split(' '))),reverse=True)
    result = marcsCakewalk(calorie)
    print(result)
