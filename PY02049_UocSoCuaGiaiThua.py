t = int(input())
for i in range(t):
    n, k = [int(x) for x in input().split()]
    ans = 0
    for i in range(1, n + 1):
        s = i
        while s % k == 0:
            ans += 1
            s //= k
    print(ans)