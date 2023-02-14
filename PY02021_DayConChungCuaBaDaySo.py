t = int(input())
for s in range (t):
    n, m, q = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    i, j, k = 0, 0, 0
    check = False
    while i < n and j < m and k < q:
        if a[i] == b[j] == c[k]:
            check = True
            print(a[i], end=" ")
            i += 1
            j += 1
            k += 1
        elif a[i] < b[j]:
            i += 1
        elif b[j] < c[k]:
            j += 1
        else:
            k += 1
    if check == False:
        print("NO")
    else:
        print()