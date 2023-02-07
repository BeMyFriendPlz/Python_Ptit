import math

def Ngto(n):
    if n < 2:
        return False
    for i in range (2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n, x = [int(x) for x in input().split()]
lst = [0]
i = 2
while len(lst) != n + 1:
    if Ngto(i):
        lst.append(i)
    i += 1
for k in lst:
    x += k
    print(x, end=' ')