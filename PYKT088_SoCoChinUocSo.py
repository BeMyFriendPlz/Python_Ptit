from math import *

n = int(input())
prime = [i for i in range(isqrt(n) + 1)]
for i in range(2, isqrt(n) + 1):
        if prime[i] == i:
            for j in range(i * i, isqrt(n) + 1, i):
                if prime[j] == j: prime[j] = i
cnt = 0
for i in range(2, isqrt(n) + 1):
    p = prime[i]
    q = prime[i // p]
    if p * q == i and q != 1 and p != q: cnt += 1
    elif prime[i] == i:
        if i ** 8 <= n: cnt += 1
print(cnt)