#!/bin/python3

import sys
import operator    
if __name__ == "__main__":
    n = int(input().strip())
    orders = []
    for orders_i in range(n):
       orders_t = []  
       for orders_temp in input().strip().split(' '):
           orders_t.append(int(orders_temp))
       orders_t.append(orders_t[0] + orders_t[1])
       orders_t.append(orders_i+1)
       orders.append(orders_t)
       cols = (2,3)
    for col in reversed(cols):
        orders= sorted(orders,key=operator.itemgetter(col))
    #orders= sorted(orders,key=operator.itemgetter(3))
    print (" ".join(map(str, [row[3] for row in orders])))


