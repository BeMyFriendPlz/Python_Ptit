n, m = [int(x) for x in input().split()]
lst = []
maximum = 0
minimum = 10000
for i in range (n):
    temp = [int(x) for x in input().split()]
    maximum = max(maximum, max(temp))
    minimum = min(minimum, min(temp))
    lst.append(temp)
check = False
for i in range (n):
    for j in range (m):
        if lst[i][j] == (maximum - minimum):
            if check == False:
                print(maximum - minimum)
            print(f"Vi tri [{i}][{j}]")
            check = True
if check == False:
    print("NOT FOUND")