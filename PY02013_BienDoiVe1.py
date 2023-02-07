while True:
    s = int(input())
    if s == 0: break
    dem = 1
    while s != 1:
        if s % 2 == 0:
            s = s / 2
        else:
            s = s * 3 + 1
        dem += 1
    print(dem)