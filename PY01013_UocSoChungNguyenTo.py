import math

def Ngto(n):
    if n < 2: return False
    for i in range (2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

t = int(input())
for i in range (t):
    a, b = [int(x) for x in input().split()]
    ucln = math.gcd(a, b)
    sum = 0
    while ucln > 0:
        sum += ucln % 10
        ucln = ucln // 10
    if Ngto(sum):
        print("YES")
    else:
        print("NO")