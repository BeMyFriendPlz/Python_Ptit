class GameThu:
    def __init__(self, a, b, c, d) -> None:
        self.ma = a
        self.ten = b
        temp1 = [int(x) for x in c.split(":")]
        temp2 = [int(x) for x in d.split(":")]
        thoiGian = (temp2[0] - temp1[0]) * 60 + (temp2[1] - temp1[1])
        self.gio = thoiGian // 60
        self.phut = thoiGian % 60
    
    def __str__(self) -> str:
        return "{} {} {} gio {} phut".format(self.ma, self.ten, self.gio, self.phut)
    
if __name__ == "__main__":
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(GameThu(input(), input(), input(), input()))
    lst.sort(key=lambda x:(-x.gio, -x.phut))
    for temp in lst:
        print(temp)