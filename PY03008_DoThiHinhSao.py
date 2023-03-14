def add(x):
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1

n = int(input())
dic = {}
for i in range (n-1):
    a, b = [int(x) for x in input().split()]
    add(a)
    add(b)
check = False
for x in dic:
    if dic[x] == n-1:
        check = True
if check:
    print("Yes")
else:
    print("No")