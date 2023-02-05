t = int(input())
for i in range (t):
    n, k = [int(x) for x in input().split()]
    lst = [int(x) for x in input().split()]
    for i in range (k - n, k):
        print(lst[i], end=' ')
    print()