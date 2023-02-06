n = int(input())
lst = [int(x) for x in input().split()]
ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        if lst[i] > lst[j]:
            ans += 1
print(ans)