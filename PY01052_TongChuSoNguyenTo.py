import math

def Ngto(n):
    if n < 2: return False
    for i in range (2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

t = int(input())
for i in range (t):
    s = input()
    sum = 0
    for c in s:
        sum += int(c)
    if Ngto(sum):
        print("YES")
    else:
        print("NO")