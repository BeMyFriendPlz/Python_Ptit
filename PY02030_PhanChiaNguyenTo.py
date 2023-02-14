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
b = {}
for i in lst : b[i] = 1
lst = list(b)
s1, s2 = sum(lst), 0
ans = -1
for i in range (len(lst)):
    s1 -= lst[i]
    s2 += lst[i]
    if Ngto(s1) and Ngto(s2):
        ans = i
        break
if ans == -1:
    print("NOT FOUND")
else:
    print(ans)