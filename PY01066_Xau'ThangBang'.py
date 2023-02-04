def check(s, r):
    for i in range (len(s)-1):
        if abs(ord(s[i]) - ord(s[i+1])) != abs(ord(r[i]) - ord(r[i+1])):
            return False
    return True

t = int(input())
for i in range (t):
    s = input()
    if check(s, s[::-1]):
        print("YES")
    else:
        print("NO")