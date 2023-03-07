import functools

class SinhVien:
    def __init__(self, id, name, score) -> None:
        self.ma = 'HS{:02d}'.format(id)
        self.ten = name
        self.diem = score

    def xepLoai(self):
        if self.diem < 5:
            return "YEU"
        elif self.diem < 7:
            return "TB"
        elif self.diem < 8:
            return "KHA"
        elif self.diem < 9:
            return "GIOI"
        else:
            return "XUAT SAC"

    def __str__(self) -> str:
        return "{} {} {} {}".format(self.ma, self.ten ,self.diem, self.xepLoai())

def cmd(a, b):
    if a.diem == b.diem:
        return 1 if a.ma > b.ma else -1
    else:
        return 1 if a.diem < b.diem else -1

n = int(input())
lst = []
for i in range(n):
    name = input()
    temp = [float(x) for x in input().split()]
    score = 0
    for j in range (len(temp)):
        if j < 2:
            score += temp[j] * 2
        else:
            score += temp[j]
    score /= 12
    lst.append(SinhVien(i+1, name, round(((score)*100+1)/100, 1)))
lst = sorted(lst, key = functools.cmp_to_key(cmd))
for i in range(n):
    print(lst[i])