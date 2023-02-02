import math

def Ngto(n):
    if n < 2: return False
    for i in range (2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

t = int(input())
for i in range (t):
    n = int(input()[-4:])
    if Ngto(n):
        print("YES")
    else:
        print("NO")