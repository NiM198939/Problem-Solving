#!/bin/python3

import sys

def maximumToys(prices, k):
    # Complete this function
    prices = sorted(prices)
    cost = 0
    toys = 0
    for i in range(len(prices)):
        cost = cost + prices[i]
        if cost >k:
            break
        toys = toys + 1
    return toys
if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    prices = list(map(int, input().strip().split(' ')))
    result = maximumToys(prices, k)
    print(result)
