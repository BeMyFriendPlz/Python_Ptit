class MonHoc:
    def __init__(self, ma, ten) -> None:
        self.ma = ma
        self.ten = ten

class LichThi:
    def __init__(self, ma, maMH, date, time, nhomThi) -> None:
        self.ma = "T{:003d}".format(ma)
        self.maMH = maMH
        self.monHoc = self.timMonHoc(maMH)
        self.date = date
        self.ngay = int(date[:2])
        self.thang = int(date[3:5])
        self.nam = int(date[-4:])
        self.time = time
        self.gio = int(time[:2])
        self.phut = int(time[-2:])
        self.nhomThi = nhomThi

    def timMonHoc(self, maMH):
        for t in mh:
            if t.ma == maMH:
                return t.ten
    
    def __str__(self) -> str:
        return "{} {} {} {} {} {}".format(self.ma, self.maMH, self.monHoc, self.date, self.time, self.nhomThi)

if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    mh = []
    for i in range(n):
        mh.append(MonHoc(input(), input()))
    lt = []
    for i in range(m):
        s = input().split()
        lt.append(LichThi(i+1, s[0], s[1], s[2], s[3]))
    lt.sort(key = lambda x : (x.nam, x.thang, x.ngay, x.gio, x.phut, x.maMH))
    print(*lt, sep="\n")