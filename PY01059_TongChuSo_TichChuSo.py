t = int(input())
for i in range (t):
    s = input()
    chan = 0
    le = 1
    check = False
    for i in range (len(s)):
        if i % 2 == 0:
            chan += int(s[i])
        else:
            if int(s[i]) != 0:
                le *= int(s[i])
                check = True
    if check:
        print(chan, le)
    else:
        print(chan, 0)