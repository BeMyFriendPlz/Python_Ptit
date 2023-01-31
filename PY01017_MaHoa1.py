t = int(input())
for i in range (t):
    s = input()
    ans = ""
    dem = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            dem += 1
        else:
            ans += str(dem) + s[i]
            dem = 1
    if dem > 0:
        ans += str(dem) + s[-1]
    print(ans)