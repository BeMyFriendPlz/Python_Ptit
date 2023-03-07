t = int(input())
for i in range(t):
    n, k = [int(x) for x in input().split()]
    lst = [int(x) for x in input().split()]
    lst.insert(lst.index(max(lst)), k)
    for i in lst:
        if i < 0:
            print(i, end=" ")
    for i in lst:
        if i >= 0:
            print(i, end=" ")
    print()