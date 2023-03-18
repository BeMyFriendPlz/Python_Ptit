import sys

a, b = [1] * 10001, []
for i in range(2, 10001):
    if a[i] == 1:
        for j in range(i * i, 10001, i):
            a[j] = 0
        b.append(i)

n = int(input())
lst = [int(x) for x in input().split()]
ans = 0
for i in lst:
    s = sys.maxsize
    for j in b:
        s = min(s, abs(i - j))
    ans = max(ans, s)
print(ans)

"""
8
13 5 8 7 9 15 26 34
"""