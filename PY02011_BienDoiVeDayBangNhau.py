import sys

n = int(input())
lst = [int(x) for x in input().split()]
ans, num = sys.maxsize, 0
for a in lst:
    s = 0
    for b in lst:
        s += abs(a - b)
    if ans > s:
        ans = s
        num = a
print(ans, num)