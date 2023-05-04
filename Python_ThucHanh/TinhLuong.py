class PhongBan:
    def __init__(self, string) -> None:
        temp = string.split()
        self.maP = temp[0]
        self.tenP = " ".join(temp[1:])

class NhanVien:
    def __init__(self, ma, ten, luongCB, soNgay) -> None:
        self.ma = ma
        self.ten = ten
        self.phongBan = self.timPhongBan(ma[3:])
        self.luongThang = self.heSoNhan(ma[0], int(ma[1:3])) * luongCB * soNgay * 1000

    def timPhongBan(self, str):
        for i in range(len(pb)):
            if pb[i].maP == str:
                return pb[i].tenP
    
    def heSoNhan(self, nhom, nam):
        if nhom == "A":
            if nam <= 3: return 10
            elif nam <= 8: return 12
            elif nam <= 15: return 14
            else: return 20
        elif nhom == "B":
            if nam <= 3: return 10
            elif nam <= 8: return 11
            elif nam <= 15: return 13
            else: return 16
        elif nhom == "C":
            if nam <= 3: return 9
            elif nam <= 8: return 10
            elif nam <= 15: return 12
            else: return 14
        elif nhom == "D":
            if nam <= 3: return 8
            elif nam <= 8: return 9
            elif nam <= 15: return 11
            else: return 13

    def __str__(self) -> str:
        return "{} {} {} {}".format(self.ma, self.ten, self.phongBan, self.luongThang)

if __name__ == "__main__":
    n = int(input())
    pb = []
    for i in range(n):
        pb.append(PhongBan(input()))
    m = int(input())
    nv = []
    for i in range(m):
        nv.append(NhanVien(input(), input(), int(input()), int(input())))
    print(*nv, sep="\n")

"""
2
HC Hanh chinh
KH Ke hoach Dau tu
2
C06HC
Tran Binh Minh
65
25
D03KH
Le Hoa Binh
59
24
"""