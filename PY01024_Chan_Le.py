def checkTong(n):
    sum = 0
    for c in n:
        sum += int(c)
    if sum % 10 == 0: return True
    return False

def checkLe(n):
    for i in range (len(n) - 1):
        if abs(ord(n[i]) - ord(n[i+1])) != 2:
            return False
    return True

t = int(input())
for i in range (t):
    n = input()
    if checkTong(n) and checkLe(n):
        print("YES")
    else:
        print("NO")