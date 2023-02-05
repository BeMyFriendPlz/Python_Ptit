def giaiThua(n):
    gt = 1
    for i in range (2, n + 1):
        gt *= i
    return gt

t = int(input())
for i in range (t):
    s = input()
    sum = 0
    for c in s:
        sum += giaiThua(int(c))
    if sum == int(s):
        print("Yes")
    else:
        print("No")