s = input()
k = int(input())
map = {}
for i in range (int(len(s) / 2)):
    if s[:2] not in map:
        map[s[:2]] = 1
    else:
        map[s[:2]] += 1
    s = s[2:]
check = False
for i in sorted(list(map)):
    if map[i] >= k:
        print(i, map[i])
        check = True
if check == False:
    print("NOT FOUND")