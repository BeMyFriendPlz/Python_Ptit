import math

l, r = [int(x) for x in input().split()]
for i in range (l, r + 1):
    for j in range (i, r + 1):
        if math.gcd(i, j) == 1:
            for k in range (j, r + 1):
                if math.gcd(j, k) == 1 and math.gcd(i, k) == 1:
                    print(f"({i}, {j}, {k})")