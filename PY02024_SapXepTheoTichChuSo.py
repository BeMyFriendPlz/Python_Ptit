import functools

def tich(n):
    tich = 1
    while n != 0 :
        tich *= n % 10
        n = int(n / 10)
    return tich

def cmd(a, b):
    if tich(a) == tich(b):
        if a > b: return 1
        else: return -1
    elif tich(a) > tich(b):
        return 1
    else:
        return -1

t = int(input())
for i in range (t):
    n = int(input())
    lst = [int(x) for x in input().split()]
    lst = sorted(lst, key = functools.cmp_to_key(cmd))
    for i in lst : print(i, end = " ")
    print()