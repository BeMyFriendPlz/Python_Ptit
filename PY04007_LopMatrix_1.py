t = int(input())
for i in range(t):
    n, m = [int(x) for x in input().split()]
    lst = [[0] * m] * n
    for i in range (n):
        lst[i] = [int(x) for x in input().split()]
    cv = []
    for i in range(m):
        temp = []
        for j in range(n):
            temp.append(lst[j][i])
        cv.append(temp)
    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(m):
                s += lst[i][k] * cv[k][j]
            print(s, end=" ")
        print()