class ThiSinh:
    def __init__(self, a, b, c) -> None:
        self.ten = a
        self.donVi = b
        self.ma = ''.join([x[0] for x in b.split()]) + ''.join([x[0] for x in a.split()])
        thoiGian = [int(x) for x in c.split(":")]
        self.vanToc = 120 / (thoiGian[0] - 6 + thoiGian[1] / 60)

    def __str__(self) -> str:
        return "{} {} {} {} Km/h".format(self.ma, self.ten, self.donVi, round(self.vanToc))

n = int(input())
lst = []
for i in range(n):
    lst.append(ThiSinh(input(), input(), input()))
lst.sort(key=lambda x:-x.vanToc)
for x in lst:
    print(x)