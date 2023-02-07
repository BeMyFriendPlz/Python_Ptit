import functools

def check(n):
    s = 0
    while n != 0 :
        s += n % 10
        n = int(n / 10)
    return s

def cmd(a, b):
    if check(a) == check(b):
        if a > b: return 1
        else: return -1
    elif check(a) > check(b): return 1
    else: return -1

t = int(input())
for i in range (t):
    n = int(input())
    lst = [int(x) for x in input().split()]
    lst = sorted(lst, key = functools.cmp_to_key(cmd))
    for i in lst : print(i, end = " ")
    print()