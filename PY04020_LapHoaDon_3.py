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