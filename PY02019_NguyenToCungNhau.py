import math

n = int(input())
lst = [int(x) for x in input().split()]
lst.sort()
for i in range (n - 1):
    for j in range(i + 1, n):
        if math.gcd(lst[i], lst[j]) == 1:
            print(lst[i], lst[j])