if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        arr = input()
        odd = ''
        even = ''
        for j in range(len(arr)):
            if j%2 == 0:
                even = even + arr[j]
            else:
                odd = odd + arr[j]
        print(str(even),str(odd))
