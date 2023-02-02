def check(s):
    for i in range (len(s)-2):
        if s[i] != s[i+2]:
            return False
    return True

t = int(input())
for i in range (t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")