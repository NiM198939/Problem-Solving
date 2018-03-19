#!/bin/python3

import sys

# def gridChallenge(grid,n):
#     # Complete this function
#     check = True
#     print(grid)
#     for i in range(n-1): 
#         for j in range(n):
#             print(i,j)
#             if grid[i][j] > grid[i+1][j]:
#                 return 'NO'
#     return 'YES'
def check_condition(grid):
    answer = 'YES'
    for i in range(grid[0] - 1):
        for j in range(grid[0]):
            if grid[1][i][j] > grid[1][i+1][j]:
                answer = 'NO'
                return answer
    return answer        
if __name__ == "__main__":
    T = int(input())
    all_grids = []
    for t in range(T):
        N = int(input())
        n = [''.join(sorted(input().strip())) for i in range(N)]
        all_grids.append([N, n])
  
    answers = []

    for grid in all_grids:
        answers.append(check_condition(grid))
    
    print('\n'.join(answers))




