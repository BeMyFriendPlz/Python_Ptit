t = int(input())
for i in range (t):
    n = int(input())
    lst = [int(x) for x in input().split()]
    dic = {}
    for i in lst:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    s = 0
    ans = 0
    for i in dic:
        if s < dic[i]:
            s = dic[i]
            ans = i
    if s > n/2: print(ans)
    else: print("NO")