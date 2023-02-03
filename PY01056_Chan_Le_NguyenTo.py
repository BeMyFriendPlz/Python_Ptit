import math

def Ngto(n):
    if n < 2:
        return False
    for i in range (2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check(s):
    sum = 0
    for i in range (len(s)):
        if i % 2 == 0 and int(s[i]) % 2 == 1:
            return False
        if i % 2 == 1 and int(s[i]) % 2 == 0:
            return False
        sum += int(s[i])
    if Ngto(sum): return True
    return False

t = int(input())
for i in range (t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")