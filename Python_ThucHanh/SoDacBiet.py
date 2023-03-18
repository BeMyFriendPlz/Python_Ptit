MOD = 10**9 + 7
t = int(input())
for i in range(t):
    n, k = [int(x) for x in input().split()]
    ans, p = 0, 1
    while k > 0:
        if k % 2 == 1:
            ans += p
            ans %= MOD
        p *= n
        k //= 2
    print(ans)

"""
3
3 4
2 12
105 564
"""