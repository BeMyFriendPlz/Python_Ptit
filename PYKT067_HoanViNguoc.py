a = [0 for x in range(15)]
b = [False for x in range(15)]
ans = []

def Try(i):
    for j in range (n, 0, -1):
        if b[j] == False:
            a[i] = j
            b[j] = True
            if i == n:
                res = [str(a[x]) for x in range(1,n+1)]
                ans.append(''.join(res))
            else:
                Try(i+1)
            b[j] = False

t = int(input())
for i in range(t):
    ans.clear()
    n = int(input())
    Try(1)
    print(len(ans))
    print(' '.join(ans))