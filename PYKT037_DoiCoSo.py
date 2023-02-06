f = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def coSoX(n, k):
    ans = ""
    while n > 0:
        num = n % k
        ans += f[num]
        n //= k
    return ans[::-1]

t = int(input())
for i in range (t):
    n, k = [int(x) for x in input().split()]
    print(coSoX(n, k))