


def getStringTransmission(n,k,stringc):
    lenc = len(stringc)
    s1 = stringc.count('1')
    s0 = stringc.count('0')
    for i in range(lenc):
        



T = int(intput())
n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
stringc = intput()
for i in range(T):
    minimumCost = getStringTransmission(n, k, stringc)
    print(minimumCost)