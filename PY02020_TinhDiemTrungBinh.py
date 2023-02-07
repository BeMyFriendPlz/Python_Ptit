n = int(input())
lst = sorted([float(x) for x in input().split()])
minlst = min(lst)
maxlst = max(lst)
while minlst in lst:
    lst.remove(minlst)
while maxlst in lst:
    lst.remove(maxlst)
ans = sum(lst) / len(lst)
print(round(ans, 2))