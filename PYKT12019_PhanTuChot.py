t = int(input())
for i in range(t):
    n = int(input())
    lst = [int(x) for x in input().split()]
    L, R = [0] * n, [0] * n
    L[0] = lst[0]
    R[n-1] = lst[n-1]
    for i in range(1, n):
        L[i] = lst[i] if lst[i] > L[i-1] else L[i-1]
    for i in range(n-2, -1, -1):
        R[i] = lst[i] if lst[i] < R[i+1] else R[i+1]
    # print(L)
    # print(R)
    ans = 0
    for i in range(n):
        if i == 0:
            if lst[i] < R[i+1]:
                ans += 1
        elif i == n-1:
            if lst[i] >= L[i-1]:
                ans += 1
        else:
            if lst[i] >= L[i-1] and lst[i] < R[i+1]:
                ans += 1
    print(ans)