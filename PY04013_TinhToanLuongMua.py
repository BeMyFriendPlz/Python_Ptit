class TramMua:
    def __init__(self, a, b) -> None:
        self.ma = "T{:02d}".format(a)
        self.ten = b
        self.thoiGian = 0
        self.luongMua = 0

    def themDuLieu(self, a, b, c):
        temp1 = [int(x) for x in a.split(":")]
        temp2 = [int(x) for x in b.split(":")]
        self.thoiGian += (temp2[0] - temp1[0]) * 60 + (temp2[1] - temp1[1])
        self.luongMua += c
    
    def trungBinh(self):
        return (self.luongMua / self.thoiGian) * 60
    
    def __str__(self) -> str:
        return "{} {} {:.02f}".format(self.ma, self.ten, self.trungBinh())
    
if __name__ == "__main__":
    n = int(input())
    lst = []
    for i in range(n):
        ten = input()
        ok = False
        for temp in lst:
            if ten == temp.ten:
                temp.themDuLieu(input(), input(), int(input()))
                ok = True
                break
        if not ok:
            tram = TramMua(len(lst) + 1, ten)
            tram.themDuLieu(input(), input(), int(input()))
            lst.append(tram)
    for temp in lst:
        print(temp)
