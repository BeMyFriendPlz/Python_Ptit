def f(x, n):
    ans = 0
    for i in range(0, 10):
        m = 10**i
        if m > n: break
        a = n//m
        b = n % m
        z = n // m % 10
        if z > x: ans += ((a // 10) + 1) * m
        elif z == x: ans += (a // 10) * m + (b + 1)
        else: ans += (a // 10) * m
        if x == 0: ans -= m
    return ans
def digitsCount(d, low, high):
    return f(d, high) - f(d, low - 1)
 
for t in range(int(input())):
    a, b = map(int, input().split())
    for i in range(0, 10): print(digitsCount(i, a, b), end=' ')
    print()

"""
3
1 9
10 456
123 2437
"""