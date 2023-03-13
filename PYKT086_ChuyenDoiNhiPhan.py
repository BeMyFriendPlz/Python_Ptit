f = '0123456789ABCDEF'

def coSoX(n, k):
    ans = ""
    while n > 0:
        num = n % k
        ans += f[num]
        n //= k
    return ans[::-1]

file = open('DATA.in', 'r')
t = int(file.readline())
for i in range (t):
    k = int(file.readline())
    s = int(file.readline(), 2)
    print(coSoX(s, k))