class TheLoai:
    def __init__(self, ma, ten) -> None:
        self.ma = "TL{:003d}".format(ma)
        self.ten = ten

class Phim:
    def __init__(self, ma, maTL, date, tenP, soTap) -> None:
        self.ma = "P{:003d}".format(ma)
        self.theLoai = self.timTheLoai(maTL)
        self.ngay = date[:2]
        self.thang = date[3:5]
        self.nam = date[-4:]
        self.tenP = tenP
        self.soTap = soTap

    def timTheLoai(self, maTL):
        for tl in theLoai:
            if tl.ma == maTL:
                return tl.ten
            
    def __str__(self) -> str:
        return "{} {} {}/{}/{} {} {}".format(self.ma, self.theLoai, self.ngay,
                                            self.thang, self.nam , self.tenP, self.soTap)


if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    theLoai = []
    for i in range(n):
        theLoai.append(TheLoai(i+1, input()))
    danhSach = []
    for i in range(m):
        danhSach.append(Phim(i+1, input(), input(), input(), int(input())))
    danhSach.sort(key = lambda x : (x.nam, x.thang, x.ngay, x.tenP, -x.soTap))
    print(*danhSach, sep="\n")