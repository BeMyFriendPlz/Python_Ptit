s = input()
map = {}
for i in range (int(len(s) / 2)):
    if s[:2] not in map:
        map[s[:2]] = 1
    else:
        map[s[:2]] += 1
    s = s[2:]
for i in map:
    print(i, map[i])