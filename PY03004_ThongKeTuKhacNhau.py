import re

n = int(input())
dic = {}
for i in range(n):
    s = re.findall("[a-zA-Z0-9]+", input())
    for temp in s:
        st = temp.lower()
        if st in dic:
            dic[st] += 1
        else:
            dic[st] = 1
ans = sorted(dic.items(), key = lambda x : (-x[1], x[0]))
for i in ans:
    print(i[0], i[1])