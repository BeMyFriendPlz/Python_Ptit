s = input()
lst = []
for i in range (0, len(s), 2):
    if i + 2 < len(s) and s[i:i+2] not in lst:
        lst.append(s[i:i+2])
for i in lst:
    print(i, end=' ')