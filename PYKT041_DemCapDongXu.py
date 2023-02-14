n = int(input())
lst = []
r = [0] * n
c = [0] * n
ans = 0
for i in range(n) :
    lst.append(input())
for i in range(n) :
    for j in range(n) :
        if lst[i][j] == 'C' :
            r[i] += 1
            c[j] += 1
for i in range(n):
    ans += r[i] * (r[i] - 1) / 2
    ans += c[i] * (c[i] - 1) / 2
print(int(ans))