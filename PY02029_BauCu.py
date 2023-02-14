import functools

n, k = [int(x) for x in input().split()]
lst = [int(x) for x in input().split()]
map, maximum = {}, 0
for i in lst:
    if i in map:
        map[i] += 1
    else:
        map[i] = 1
    maximum = max(maximum, map[i])
x, ans = 0, 0
for i in map:
    if x < map[i] and map[i] != maximum:
        x = map[i]
        ans = i
if ans == 0:
    print("NONE")
else:
    print(ans)