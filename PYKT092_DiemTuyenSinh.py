class ThiSinh:
    def __init__(self, ma, ten, diem, danToc, khuVuc) -> None:
        self.ma = "TS{:02d}".format(ma)
        self.ten = " ".join([x.lower().title() for x in ten.split()])
        self.diem = diem
        if danToc != 'Kinh':
            self.diem += 1.5       
        if khuVuc == "1":
            self.diem += 1.5
        elif khuVuc == "2":
            self.diem += 1
        if self.diem >= 20.5:
            self.trangThai = "Do"
        else:
            self.trangThai = "Truot"
    
    def __str__(self) -> str:
        return "{} {} {:.1f} {}".format(self.ma, self.ten, self.diem, self.trangThai)
    
if __name__ == "__main__":
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(ThiSinh(i+1, input(), float(input()), input(), input()))
    lst.sort(key=lambda x : (-x.diem, x.ma))
    print(*lst,sep='\n')