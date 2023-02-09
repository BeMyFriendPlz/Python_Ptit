n = int(input())
lst = []
for i in range (n):
    lst.append([int(x) for x in input().split()])
k = int(input())
up = down = 0
for i in range (n):
    for j in range (n):
        if j < i:
            down += lst[i][j]
        if j > i:
            up += lst[i][j]
if abs(up - down) > k:
    print("NO")
else:
    print("YES")
print(abs(up- down))