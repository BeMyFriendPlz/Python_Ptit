a = []
def Try():
    for j in range(n, 0, -1):
        if len(a) > 0 and a[-1] < j: continue
        a.append(j)
        if sum(a) == n:
            strng = str(a[0])
            for temp in range(1, len(a)):
                strng += (" " + str(a[temp]))
            ans.append("(" + strng + ")")
        elif sum(a) < n:
            Try()
        a.pop()

t = int(input())
ans = []
for i in range(t):
    ans.clear()
    a.clear()
    n = int(input())
    Try()
    print(len(ans))
    print(*ans)

"""
2
4
5
"""