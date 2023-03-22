lst = []
while True:
    try:
        s = input().lower().split()
        s[0] = s[0].title()
        if s[-1] != "." and s[-1] != "!" and s[-1] != "?":
            ans = " ".join(s)
        else:
            ans = " ".join(s[:-1])
            ans += s[-1]
        if ans[-1] != "." and ans[-1] != "!" and ans[-1] != "?":
            ans += "."
        lst.append(ans)
    except:
        break
print(*lst, sep="\n")