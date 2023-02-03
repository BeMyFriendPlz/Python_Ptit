t = int(input())
for i in range (t):
    n = int(input())
    dem = 0
    while n % 7 != 0 and dem < 1000:
        n += int(str(n)[::-1])
        dem += 1
    if dem != 1000:
        print(n)
    else:
        print(-1)