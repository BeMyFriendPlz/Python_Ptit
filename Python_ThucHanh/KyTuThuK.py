def findCharacter(n, k):
    if k > 2**n: return findCharacter(n - 1, k - 2**n)
    elif k < 2**n: return findCharacter(n - 1, k)
    else: return n

t = int(input())
for i in range(t):
    n, k = [int(x) for x in input().split()]
    print(chr(ord('A') + findCharacter(n, k)))

"""
2
3 2
4 8
"""