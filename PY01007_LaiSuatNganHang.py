import math

t = int(input())
for i in range (t):
    n, x, m = [float(x) for x in input().split()]
    ans = math.log(m / n, (100 + x) / 100)
    print(int(ans) if ans == int(ans) else int(ans + 1))