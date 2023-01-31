t = int(input())
for i in range (t):
    s = input()
    ans = ""
    i = 0
    while i < len(s)-1:
        a, b = s[i], s[i+1]
        ans += a * int(b)
        i += 2
    print(ans)