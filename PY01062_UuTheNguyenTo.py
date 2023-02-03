import math

def Ngto(n):
    if n < 2:
        return False
    for i in range (2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check(s):
    lst = ['2', '3', '5', '7']
    dem = 0
    for i in s:
        if i in lst: 
            dem += 1
    if (dem * 2) > len(s):
        return True
    else: 
        return False

t = int(input())
for i in range (t):
    s = input()
    if Ngto(len(s)) and check(s):
        print("YES")
    else:
        print("NO")