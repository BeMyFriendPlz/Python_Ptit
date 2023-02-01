s = input()
ans = ""
for i in range (1,len(s)):
    ans += s[-i]
    if(i % 3 == 0):
        ans += ","
ans += s[0]
print(ans[::-1])