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
    sum = 0
    for c in s:
        if c not in lst: 
            return False
        sum += int(c)
    if Ngto(sum): return True
    return False

t = int(input())
for i in range (t):
    s = input()
    if Ngto(int(s)) and Ngto(int(s[::-1])) and check(s):
        print("Yes")
    else:
        print("No")