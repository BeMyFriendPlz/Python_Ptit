def check(a, b):
    if len(a) != len(b): return False
    for i in a:
        if i not in b:
            return False
    return True

n, m = [int(x) for x in input().split()]
lst1 = list({int(x) for x in input().split()})
lst2 = list({int(x) for x in input().split()})
if check(lst1, lst2):
    print("YES")
else:
    print("NO")