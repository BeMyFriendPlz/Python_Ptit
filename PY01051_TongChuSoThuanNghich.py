def check(s):
    for i in range (int(len(s)/2)):
        if s[i] != s[-(i+1)]:
            return False
    return True

t = int(input())
for i in range (t):
    s = input()
    sum = 0
    for c in s:
        sum += int(c)
    if len(str(sum)) > 1 and check(str(sum)):
        print("YES")
    else:
        print("NO")