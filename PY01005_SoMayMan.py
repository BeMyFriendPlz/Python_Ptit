n = input()
s = 0
for c in n:
    if c == '4' or c == '7':
        s += 1
if s == 4 or s == 7:
    print("YES")
else:
    print("NO")