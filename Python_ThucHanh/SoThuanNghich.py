a, b, m = map(int, input().split())

if m > 3:
    count = 0
    for i in [0, 1]:
        if a <= i and i <= b:
            count += 1
    print(count)

elif m == 3:
    count = 0
    for i in [0, 1, 6643, 1422773, 5415589]:
        if a <= i and i <= b:
            count += 1
    print(count)

elif m == 2:
    count = 0
    for i in range(1, 10000):
        s1 = bin(i)[2:]
        s2 = ''.join(reversed(s1))
        arr = [s1+s2, s1+'0'+s2, s1+'1'+s2]
        for j in arr:
            x = int(j, 2)
            if a <= x and x <= b:
                count += 1
    for i in [0, 1]:
        if a <= i and i <= b:
            count += 1
    print(count)

else:
    print(0)