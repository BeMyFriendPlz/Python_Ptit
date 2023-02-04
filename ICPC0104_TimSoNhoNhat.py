import re

t = int(input())
for i in range (t):
    s = re.findall("\d+", input())
    num = [int(x) for x in s]
    print(min(num))