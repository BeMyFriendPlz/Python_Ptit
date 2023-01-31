s = input()
chuHoa = chuThuong = 0
for c in s:
    if c.islower():
        chuThuong += 1
    else:
        chuHoa += 1
if chuThuong >= chuHoa:
    print(s.lower())
else:
    print(s.upper())