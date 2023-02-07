lst = []
while len(lst) != 10:
    lst = lst + [int(x) for x in input().split()]
ans = []
for i in range (10):
    md = lst[i] % 42
    if md not in ans:
        ans.append(md)
print(len(ans))