n, k = [int(x) for x in input().split()]
st = {x for x in input().split()}
lst = sorted(list(st))
n = len(lst)
a = [0] * (k + 1)

def Try(i):
    for j in range(a[i - 1] + 1, n + 1):
        a[i] = j
        if i == k:
            for i in range (1, len(a)):
                print(lst[a[i] - 1], end=' ')
            print()
        else:
            Try(i+1)

Try(1)