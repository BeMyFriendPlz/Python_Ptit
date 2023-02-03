import math

def Ngto(n):
    if n < 2:
        return False
    for i in range (2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

lst = ['2', '3', '5', '7']

def check(s):
    for i in range (len(s)):
        if Ngto(i) == True and s[i] not in lst:
            return False
        if Ngto(i) == False and s[i] in lst:
            return False
    return True

t = int(input())
for i in range (t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")