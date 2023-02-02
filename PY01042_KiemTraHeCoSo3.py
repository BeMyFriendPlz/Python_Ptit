lst = ['0', '1', '2']

def check(s):
    for c in s:
        if c not in lst:
            return False
    return True

t = int(input())
for i in range (t):
    s = input()
    if check(s): print("YES")
    else: print("NO")