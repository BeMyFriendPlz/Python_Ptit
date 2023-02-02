t = int(input())
for i in range (t):
    s = input()
    tich = 1
    for c in s:
        if int(c) != 0:
            tich *= int(c)
    print(tich)