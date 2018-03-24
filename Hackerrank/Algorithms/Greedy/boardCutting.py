#!/bin/python3

import sys
total_sum = 1000000007
def boardCutting(sorted_list):
    # Complete this function
    hc = 1
    vc = 1
    total_cost = 0
    for i in range(len(sorted_list)):
        if sorted_list[i].c =='a':
            total_cost = total_cost + vc*sorted_list[i].n
            hc = hc + 1
        else:
            total_cost = total_cost + hc*sorted_list[i].n
            vc = vc + 1
    return total_cost
class number:
    def __init__(self, n, c):
        self.n = n
        self.c = c
if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        m, n = input().strip().split(' ')
        m, n = [int(m), int(n)]
        m_list = input().strip().split(' ')
        cost = []
        for list_item in m_list:
            cost.append(number(int(list_item),'a'))
        n_list = input().strip().split(' ')
        cost_x = []
        for list_item in n_list:
            cost.append(number(int(list_item),'b'))
        sorted_list = sorted(cost, key=lambda number: number.n, reverse=True)
        result = boardCutting(sorted_list)
        print(result%total_sum)
