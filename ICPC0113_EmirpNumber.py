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
    s = int(input())
    ans = []
    for i in range (10, s):
        if i != int(str(i)[::-1]) and Ngto(i) and Ngto(int(str(i)[::-1])):
            if i not in ans and int(str(i)[::-1]) not in ans and int(str(i)[::-1]) < s:
                ans.append(i)
                ans.append(int(str(i)[::-1]))
    for n in ans:
        print(n, end=" ")
    print()