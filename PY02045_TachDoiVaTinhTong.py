def tinhTong(s1, s2):
    return str(int(s1) + int(s2))

s = input()
while len(s) > 1:
    n = len(s)
    s = tinhTong(s[:n//2], s[n//2:])
    print(s)