s = input()
n = len(s)
a = [0] * n

def Try(ans, i):
    if i == n:
        print(ans)
        return
    for j in range (n):
        if a[j] == 0:
            a[j] = 1
            Try(ans + s[j], i+1)
            a[j] = 0

Try("",0)