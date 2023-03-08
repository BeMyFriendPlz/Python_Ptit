def solve(a, b):
    sum = 0
    for i in range(max(a-1, 0), min(a+2, n)):
        for j in range(max(b-1, 0), min(b+2, m)):
            if check[i][j] == 0 and not (i == a and j == b):
                sum += lst[i][j]
                check[i][j] = 1
    return sum

n, m = [int(x) for x in input().split()]
lst = []
for i in range(n):
    lst.append([int(x) for x in input().split()])
ans = 0
check = []
for i in range(n):
    check.append([0] * m)
for i in range(n):
    for j in range(m):
        if lst[i][j] == -1:
            ans += solve(i, j)
print(ans)