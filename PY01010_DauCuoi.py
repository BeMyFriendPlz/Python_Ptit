t = int(input())
for i in range (t):
    s = input()
    if s[:2] == s[-2:]:
        print("YES")
    else:
        print("NO")