n, m = [int(x) for x in input().split()]
lst = []
for i in range(n):
    lst.append([int(x) for x in input().split()])
d = []
sub = abs(n-m)
while sub > 0:
    if n > m:
        d.append(2*sub - 2)
    else:
        d.append(2*sub - 1)
    sub -= 1
if n > m:
    for i in range(n) :
        if not(i in d) :
            for j in range(m) :
                print(lst[i][j], end = ' ')
            print()
else:
    for i in range(n) :
        for j in range(m) :
            if not(j in d) :
                print(lst[i][j], end = ' ')
        print()