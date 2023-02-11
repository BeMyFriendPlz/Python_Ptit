n, m = [int(x) for x in input().split()]
lst1 = list({int(x) for x in input().split()})
lst2 = list({int(x) for x in input().split()})
map = {}
for i in lst1:
    map[i] = 1
for i in lst2:
    if i not in map:
        map[i] = 1
    else:
        map[i] += 1
for i in sorted(list(map)):
    if map[i] == 2:
        print(i, end=' ')
print()
for i in sorted(lst1):
    if map[i] == 1:
        print(i, end=' ')
print()
for i in sorted(lst2):
    if map[i] == 1:
        print(i, end=' ')