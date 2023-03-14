import re

n = int(input())
lst = []
for i in range(n):
    lst += [int(x) for x in re.findall("\d+", input())]
lst.sort()
for x in lst:
    print(x)