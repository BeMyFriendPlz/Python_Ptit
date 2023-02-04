def check(a, b):
    for i in range (len(a)):
        if a[i] > b[i]: return False
    return True

t = int(input())
for i in range (t):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a.sort()
    b.sort()
    if check(a, b):
        print("YES")
    else:
        print("NO")