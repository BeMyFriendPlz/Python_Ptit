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
mp = {}
for num in lst:
    if Ngto(num):
        if num not in mp:
            mp[num] = 1
        else:
            mp[num] += 1
for ans in mp:
    print(ans, mp.get(ans))
