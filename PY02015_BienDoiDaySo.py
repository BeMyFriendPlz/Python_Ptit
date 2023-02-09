def check(lst):
    return lst[0] == lst[1] and lst[1] == lst[2] and lst[2] == lst[3]

while True:
    lst = [int(x) for x in input().split()]
    if check(lst) and lst[0] == 0:
        break
    dem = 0
    while not check(lst):
        temp = lst[0]
        for i in range (3):
            lst[i] = abs(lst[i] - lst[i+1])
        lst[3] = abs(lst[3] - temp)
        dem += 1
    print(dem)