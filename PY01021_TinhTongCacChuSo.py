import re

t = int(input())
for i in range (t):
    s = input()
    num = re.findall("\d", s)
    string = re.findall("\D", s)
    lst1 = [int(x) for x in num]
    lst2 = "".join(sorted([x for x in string]))
    print(lst2 + str(sum(lst1)))