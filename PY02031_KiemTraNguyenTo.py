import math

def Ngto(n):
    if n < 2:
        return False
    for i in range (2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n, m = [int(x) for x in input().split()]
lst = []
for i in range (n):
    lst.append([int(x) for x in input().split()])
for i in range (n):
    for j in range (m):
        if Ngto(lst[i][j]):
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()