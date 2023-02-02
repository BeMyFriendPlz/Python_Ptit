def check(s):
    k = 0
    while k < (len(s)-1) and s[k] < s[k+1]:
        k += 1
    if k+1 == len(s): return False
    else:
        while k < (len(s)-1) and s[k] > s[k+1]:
            k += 1
        if k+1 == len(s): return True
        return False

t = int(input())
for i in range (t):
    s = input()
    if check(s): print("YES")
    else: print("NO")