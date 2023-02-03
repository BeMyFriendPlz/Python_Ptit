b = ['0', '2', '4', '6', '8']

t = int(input())
for i in range (t):
    n = int(input())
    ans = []
    Q = ['00', '22', '44', '66', '88']
    while len(Q) > 0:
        temp = Q.pop(0)
        if len(temp) < 6:
            for i in b:
                Q.append(i + temp + i)
        if temp[0] != "0":
            ans.append(int(temp))
    ans.sort()
    for i in ans:
        if i < n:
            print(i, end=' ')
        else:
            break
    print()