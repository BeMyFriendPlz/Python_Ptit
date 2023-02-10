import math

class PhanSo:
    def __init__(self, a, b):
        self.tu = a
        self.mau = b

    def toiGian(self):
        ucln = math.gcd(self.tu, self.mau)
        return "{}/{}".format(self.tu // ucln, self.mau // ucln)

    def tinhTong(self, ps):
        tu = self.tu * ps.mau + ps.tu * self.mau
        mau = self.mau * ps.mau
        return PhanSo(tu, mau)

if __name__ == '__main__':
    lst = [int(x) for x in input().split()]
    ps1 = PhanSo(lst[0], lst[1])
    ps2 = PhanSo(lst[2], lst[3])
    ps3 = ps1.tinhTong(ps2)
    print(ps3.toiGian())