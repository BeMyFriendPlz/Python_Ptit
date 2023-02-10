import math

class PhanSo:
    def __init__(self, a, b):
        self.tu = a
        self.mau = b

    def toiGian(self):
        ucln = math.gcd(self.tu, self.mau)
        return "{}/{}".format(self.tu // ucln, self.mau // ucln)

if __name__ == '__main__':
    tu, mau = [int(x) for x in input().split()]
    ps = PhanSo(tu, mau)
    print(ps.toiGian())