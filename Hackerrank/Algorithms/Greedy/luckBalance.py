#!/bin/python3

import sys

def luckBalance(n, k, total_luck, important_ones):
    # Complete this function
    important_ones = sorted(important_ones, reverse= True)
    if k>=len(important_ones):
        for i in range(len(important_ones)):
            total_luck = total_luck + important_ones[i]
    else:
        for i in range(k):
            total_luck = total_luck + important_ones[i]
        for i in range(len(important_ones)-k):
            total_luck = total_luck - important_ones[k+i]
    return total_luck

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    important_ones = []
    non_important_ones = []
    total_luck = 0
    for contests_i in range(n):
       contests_t = [int(contests_temp) for contests_temp in input().strip().split(' ')]
       if contests_t[1] == 0:
           total_luck = total_luck + contests_t[0]
       else:
           important_ones.append(contests_t[0])
    result = luckBalance(n, k, total_luck, important_ones)
    print(result)
