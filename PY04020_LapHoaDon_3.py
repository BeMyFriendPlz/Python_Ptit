import math

def ngTo(s):
    if s < 2: return False
    for i in range (2, int(math.sqrt(s)) + 1):
        if s % i == 0:
            return False
    return True

n = int(input())
print(ngTo(n))