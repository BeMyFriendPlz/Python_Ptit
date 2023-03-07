import functools

class KhachHang:
    def __init__(self, id, name, water) -> None:
        self.ma = "KH{:02d}".format(id)
        self.ten = name
        self.chiSo = water

    def tongTien(self):
        tien = 0
        phuPhi = 0
        if self.chiSo > 100:
            tien = 50 * 100 + 50 * 150 + (self.chiSo - 100) * 200
            phuPhi = 5/100
        elif self.chiSo > 50:
            tien = 50 * 100 + (self.chiSo - 50) * 150
            phuPhi = 3/100
        else:
            tien = self.chiSo * 100
            phuPhi = 2/100
        return round(tien * (1 + phuPhi))
    
    def __str__(self) -> str:
        return "{} {} {}".format(self.ma, self.ten, self.tongTien())

def cmd(a, b):
    if a.tongTien() < b.tongTien():
        return 1
    else:
        return -1

if __name__ == '__main__':
    n = int(input())
    lst = []
    for i in range(n):
        name, chiSoCu, chiSoMoi = input(), int(input()), int(input())
        lst.append(KhachHang(i+1, name, chiSoMoi - chiSoCu))
    lst.sort(key=functools.cmp_to_key(cmd))
    for i in lst:
        print(i)