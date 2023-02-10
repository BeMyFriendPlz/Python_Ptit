import math

def Ngto(n):
    if n < 2:
        return False
    for i in range (2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
lst = [int(x) for x in input().split()]
index = [0] * n
temp = []
for i in range (n):
    if Ngto(lst[i]):
        temp.append(lst[i])
        index[i] = 1
temp.sort(reverse=True)
for i in range(n):
    if index[i] == 1:
        print(temp[-1], end=' ')
        temp.pop()
    else:
        print(lst[i], end=' ')