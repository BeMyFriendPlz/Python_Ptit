def deQuy(n, k):
    if k > 2**n: return deQuy(n - 1, k - 2 ** n)
    elif k < 2**n: return deQuy(n - 1, k)
    else: return n

t = int(input())
for i in range(t):
    n, k = [int(x) for x in input().split()]
    print(chr(ord('A') + deQuy(n, k)))