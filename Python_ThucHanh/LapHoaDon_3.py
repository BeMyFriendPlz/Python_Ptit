class MatHang:
    def __init__(self, ma, ten, soLuong, donGia, chietKhau) -> None:
        self.ma = ma
        self.ten = ten
        self.soLuong = soLuong
        self.donGia = donGia
        self.chietKhau = chietKhau
        self.tongTien = soLuong * donGia - chietKhau
    
    def __str__(self) -> str:
        return "{} {} {} {} {} {}".format(self.ma, self.ten, self.soLuong, self.donGia, self.chietKhau, self.tongTien)

n = int(input())
lst = []
for i in range(n):
    lst.append(MatHang(input(), input(), int(input()), int(input()), int(input())))
lst.sort(key=lambda x:-x.tongTien)
for x in lst:
    print(x)

"""
3
ML01
May lanh SANYO
12
4000000
2400000
ML02
May lanh HITACHI
4
2550000000
0
ML03
May lanh NATIONAL
5
3000000
150000
"""