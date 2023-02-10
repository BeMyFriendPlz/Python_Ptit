n = int(input())
lst = []
while True:
    lst += [int(x) for x in input().split()]
    if len(lst) == n: break
chan, le = [], []
index = [0] * n
for i in range(n):
    if (lst[i] % 2) == 0:
        chan.append(lst[i])
        index[i] = 1
    else:
        le.append(lst[i])
chan = sorted(chan, reverse=True)
le = sorted(le)
for i in range(n):
    if index[i] == 1:
        print(chan[-1], end=' ')
        chan.pop()
    else:
        print(le[-1], end=' ')
        le.pop()