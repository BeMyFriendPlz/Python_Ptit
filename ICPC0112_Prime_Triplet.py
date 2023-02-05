import math

def Ngto(n):
    if n < 2:
        return False
    for i in range (2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
for i in range (t):
    n = int(input())
    dem = 0
    for i in range(2, n - 6):
        if Ngto(i) and Ngto(i+2) and Ngto(i+6):
            dem += 1
        if Ngto(i) and Ngto(i+4) and Ngto(i+6):
            dem += 1
    print(dem)