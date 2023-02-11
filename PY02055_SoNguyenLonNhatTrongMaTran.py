import math

def Ngto(n):
    if n < 2:
        return False
    for i in range (2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n, m = [int(x) for x in input().split()]
lst = []
maximum = 0
for i in range (n):
    temp = [int(x) for x in input().split()]
    for j in range (m):
        if Ngto(temp[j]):
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