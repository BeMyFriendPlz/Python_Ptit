import math

def Ngto(n):
    if n < 2: return False
    for i in range (2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

lst = ['2', '3', '5', '7']

t = int(input())
for i in range (t):
    s = input()
    ngto = 0
    for c in s:
        if c in lst: ngto += 1
    if Ngto(len(s)) and ngto > (len(s) - ngto):
        print("YES")
    else:
        print("NO")