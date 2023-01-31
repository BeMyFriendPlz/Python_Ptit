a, k, n = [int(x) for x in input().split()]
if a >= n:
    print("-1")
else:
    x = 1
    dem = 0
    while True:
        if x * k > n: break
        b = x * k - a
        if b > 0: 
            print(b, end=' ')
            dem += 1
        x += 1
    if dem == 0: print("-1")