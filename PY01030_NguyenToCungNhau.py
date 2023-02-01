import math

n, k = [int(x) for x in input().split()]
dem = 0
for i in range (10 ** (k - 1), (10 ** k) -1):
    if math.gcd(n, i) == 1:
        print(i, end = " ")
        dem += 1
        if dem % 10 == 0:
            print()