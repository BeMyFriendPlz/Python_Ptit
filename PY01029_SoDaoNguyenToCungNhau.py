import math

t = int(input())
for i in range (t):
    n = input()
    d = n[::-1]
    if math.gcd(int(n), int(d)) == 1:
        print("YES")
    else:
        print("NO")