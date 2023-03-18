import sys

n = int(input())
lst = [int(x) for x in input().split()]
ans, p = sys.maxsize, 0
for i in lst:
    s = 0
    for j in lst:
        s += abs(i - j)
    if ans > s:
        ans = s
        p = i
print(ans, p)

"""
8
13 5 8 7 9 15 26 34
"""