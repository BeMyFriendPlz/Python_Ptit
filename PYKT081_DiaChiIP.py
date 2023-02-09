def check(s):
    if len(s) != 4:
        return False
    for i in s:
        try:
            if int(i) > 255 or int(i) < 0:
                return False
        except:
            return False
    return True

t = int(input())
for i in range(t):
    s = [x for x in input().split('.')]
    if check(s):
        print("YES")
    else:
        print("NO")