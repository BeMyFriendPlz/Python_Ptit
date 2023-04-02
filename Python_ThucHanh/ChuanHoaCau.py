lst = []
while True:
    try:
        s = [x.lower() for x in input().split()]
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

"""
Chuong trinh Dao Tao CLC nganh CNTT duoc Thiet     Ke theo chuan quoc te.
co 03 chuyen nganh la: Cong  nghe phan mem, Tri tue nhan tao va An toan thong tin
muc tieu cua chuong trinh la trang bi cho sinh vien cac ky nang nghe nghiep
moi    CAC BAN danG ky     thaM giA !
"""