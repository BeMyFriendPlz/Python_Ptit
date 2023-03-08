n = int(input())
lst = []
for i in range (n):
    lst.append([int(x) for x in input().split()])
if n == 2:
    print("1 1")
else:
    ans = [0] * n
    ans[0] = (lst[0][1] + lst[0][2] - lst[1][2]) // 2
    for i in range (1, n):
        ans[i] = lst[0][i] - ans[0]
    print(*ans)