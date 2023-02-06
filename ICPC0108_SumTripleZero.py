t = int(input())
for i in range (t):
    n = int(input())
    lst = sorted([int(x) for x in input().split()])
    dem = 0
    for i in range (0, n - 2):
        l = i + 1
        r = len(lst) - 1
        x = lst[i]
        while l < r:
            if x + lst[l] + lst[r] == 0:
                dem += 1
                l += 1
            elif x + lst[l] + lst[r] < 0:
                l += 1
            else:
                r -= 1
    print(dem)