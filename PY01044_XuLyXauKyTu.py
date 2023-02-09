s1 = set([x.lower() for x in input().split()])
s2 = set([x.lower() for x in input().split()])
giao = []
hop = []
for i in s1:
    giao.append(i)
for i in s2:
    if i in giao:
        hop.append(i)
    else:
        giao.append(i)
giao.sort()
hop.sort()
for i in giao:
    print(i, end=' ')
print()
for i in hop:
    print(i, end=' ')