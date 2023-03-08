class ThiSinh:
    def __init__(self, a, b, c, d):
        self.ma = "TS0" + str(a)
        self.name = b
        self.lyThuyet = c
        while(self.lyThuyet > 10):
            self.lyThuyet /= 10
        self.thucHanh = d
        while(self.thucHanh > 10):
            self.thucHanh /= 10
    
    def trungBinh(self):
        return (self.lyThuyet + self.thucHanh) / 2
    
    def xepLoai(self):
        if self.trungBinh() < 5:
            return "TRUOT"
        elif self.trungBinh() < 8:
            return "CAN NHAC"
        elif self.trungBinh() < 9.5:
            return "DAT"
        else:
            return "XUAT SAC"

    def __str__(self) -> str:
        return "{} {} {:.2f} {}".format(self.ma, self.name, self.trungBinh(), self.xepLoai())
    
if __name__ == "__main__":
    n = int(input())
    lst = []
    for i in range(n):
        ts = ThiSinh(i+1, input(), float(input()), float(input()))
        lst.append(ts)
    lst.sort(key=lambda x:-x.trungBinh())
    for i in lst:
        print(i)