#!/bin/python3
#use lexicographic  sorting 
#Append zeros in front to do the soring
import sys
# class bigsort():
#     def __init__(self, big_num, len_big_num):
#         self.big_num = big_num
#         self.len_big_num = len_big_num
# def bigSorting(arr,max_len):
#     # Complete this function
#     arr = sorted(arr, key=lambda bigsort: bigsort.big_num)
#     result = []
#     for i in range(len(arr)):
#         result.append(arr[i].big_num[arr[i].len_big_num:])
#     return result
# if __name__ == "__main__":
#     n = int(input().strip())
#     arr = []
#     arr_i = 0
#     max_len = 0 
#     post_arr = []
#     
#     for arr_i in range(n):
#        arr_t = str(input().strip())
#        if max_len < len(arr_t):
#            max_len = len(arr_t)
#        arr.append(arr_t)
#        
#     for j in range(len(arr)):
#         len_arr = max_len - len(arr[j])
#         string_t = '0'*len_arr + arr[j]
#         post_arr.append(bigsort(string_t,len_arr))
#     result = bigSorting(post_arr,max_len)
#     print ("\n".join(map(str, result)))
    

#!/bin/python3

import sys



def comparefunc(x,y):
    
    m = len(x)
    n = len(y)
    if m == n:
        for i in range(m):
            if x[i] != y[i]:
                return int(x)-int(y) 
    return m-n

def bigSorting(arr):
    # Complete this function
    for i in sorted(sorted(arr), key=len):
        print(i)
        
if __name__ == "__main__":
    n = int(input())
    arr = []
    arr_i = 0
    for arr_i in range(n):
       arr_t = raw_input()
       arr.append(arr_t)
    bigSorting(arr)
    

    
    
    
    


