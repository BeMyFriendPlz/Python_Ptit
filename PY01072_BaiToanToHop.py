n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [0] * (k + 1)
a = list(set(a))
a.sort()
n = len(a)
ans = [0] * (k + 1)

def Try(i):
    for j in range (ans[i-1] + 1, n - k + i + 1):
        ans[i] = j
        if i == k:
            for num in range (1, len(ans)):
                print(a[ans[num] - 1], end=' ')
            print()
        else:
            Try(i+1)

Try(1)