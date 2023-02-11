s = input()
lst = []
for i in range (int(len(s) / 2)):
    if s[:2] not in lst:
        lst.append(s[:2])
    s = s[2:]
lst.sort()
for i in lst:
    print(i, end=' ')