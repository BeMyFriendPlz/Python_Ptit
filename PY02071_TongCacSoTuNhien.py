def Try(k, lst):
    for i in range (k, 0, -1):
        if len(lst) > 0 and lst[-1] < i: continue
        lst.append(i)
        if sum(lst) == n:
            strng = str(lst[0])
            for temp in range(1, len(lst)):
                strng += (" " + str(lst[temp]))
            ans.append("(" + strng + ")")
        else:
            Try(k-i, lst)
        lst.pop()

t = int(input())
for i in range(t):
    n = int(input())
    ans = []
    Try(n, [])
    print(len(ans))
    print(*ans)
