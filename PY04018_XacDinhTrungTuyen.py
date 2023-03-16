class GiaoVien:
    def __init__(self, id, ten, maXetTuyen, d1, d2) -> None:
        self.id = "GV{:02d}".format(id)
        self.ten = ten
        if maXetTuyen[0] == "A":
            self.mon = "TOAN"
        elif maXetTuyen[0] == "B":
            self.mon = "LY"
        else:
            self.mon = "HOA"
        if maXetTuyen[1] == "1":
            self.diemTB = 2 + d1 * 2 + d2
        elif maXetTuyen[1] == "2":
            self.diemTB = 1.5 + d1 * 2 + d2
        elif maXetTuyen[1] == "3":
            self.diemTB = 1 + d1 * 2 + d2
        else:
            self.diemTB = d1 * 2 + d2
        if self.diemTB > 18:
            self.xetTuyen = "TRUNG TUYEN"
        else:
            self.xetTuyen = "LOAI"
    
    def __str__(self) -> str:
        return "{} {} {} {:.1f} {}".format(self.id, self.ten, self.mon, self.diemTB, self.xetTuyen)

n = int(input())
lst = []
for i in range(n):
    lst.append(GiaoVien(i+1, input(), input(), float(input()), float(input())))
lst.sort(key=lambda x:-x.diemTB)
for x in lst:
    print(x)
