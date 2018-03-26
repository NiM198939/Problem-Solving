






T = int(intput())
n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
stringc = intput()
for i in range(T):
    
minimumCost = getStringTransmission(n, k, c)
print(minimumCost)