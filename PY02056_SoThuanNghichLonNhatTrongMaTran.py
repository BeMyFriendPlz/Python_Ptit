def thuanNghich(n):
    if n < 10: return False
    m = int(str(n)[::-1])
    if m == n:
        return True
    else:
        return False

n, m = [int(x) for x in input().split()]
lst = []
maximum = 0
for i in range (n):
    temp = [int(x) for x in input().split()]
    for j in range (m):
        if thuanNghich(temp[j]):
            maximum = max(maximum, temp[j])
    lst.append(temp)
if maximum == 0:
    print("NOT FOUND")
else:
    print(maximum)
    for i in range (n):
        for j in range (m):
            if lst[i][j] == maximum:
                print(f"Vi tri [{i}][{j}]")