lst = [1, 1]

for i in range (2, 93):
    lst.append(lst[i-1] + lst[i-2])

t = int(input())
for i  in range(t):
    a, b = [int(x) for x in input().split()]
    for i in range (a, b+1):
        print(lst[i-1], end=' ')
    print()