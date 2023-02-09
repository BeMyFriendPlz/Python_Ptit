def min(lst):
    res = lst[0]
    for i in lst:
        if res != i:
            return res
        res += 1
    return lst[-1] + 1

n = int(input())
lst = sorted([int(x) for x in input().split()])
print(min(lst))