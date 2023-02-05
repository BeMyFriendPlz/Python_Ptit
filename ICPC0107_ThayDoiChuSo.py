def minNum(x, y, s):
    return int(s.replace(y, x))

def maxNum(x, y, s):
    return int(s.replace(x, y))

t = int(input())
for i in range (t):
    x, y = [x for x in input().split()]
    if int(x) > int(y): x, y = y, x
    s1 = input().strip()
    if s1.count(' '): s1, s2 = s1.split()
    else: s2 = input()
    print(minNum(x, y, s1) + minNum(x, y, s2), maxNum(x, y, s1) + maxNum(x, y, s2))