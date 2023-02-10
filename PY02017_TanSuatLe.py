t = int(input())
for i in range (t):
    n = int(input())
    lst = [int(x) for x in input().split()]
    map = {}
    for i in range(n):
        if lst[i] not in map:
            map[lst[i]] = 1
        else:
            map[lst[i]] += 1
    for i in map:
        if map[i] % 2 == 1:
            print(i)
            break