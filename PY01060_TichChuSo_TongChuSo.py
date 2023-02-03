t = int(input())
for i in range (t):
    s = input()
    chan = 1
    le = 0
    check = False
    for i in range (len(s)):
        if i % 2 == 1:
            le += int(s[i])
        else:
            if int(s[i]) != 0:
                chan *= int(s[i])
                check = True
    if check:
        print(chan, le)
    else:
        print(chan, 0)