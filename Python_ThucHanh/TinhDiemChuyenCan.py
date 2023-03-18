class SinhVien:
    def __init__(self, id, name, clas) -> None:
        self.id = id
        self.name = name
        self.clas = clas
        self.diemcc = 10

    def diemDanh(self, cc):
        m = cc.count('m')
        v = cc.count('v')
        self.diemcc -=  (m + v*2)
        if self.diemcc < 0: self.diemcc = 0

    def __str__(self) -> str:
        return "{} {} {} {}".format(self.id, self.name, self.clas, self.diemcc) + (" KDDK" if self.diemcc == 0 else "")

n = int(input())
lst = []
for i in range(n):
    lst.append(SinhVien(input(), input(), input()))
for i in range(n):
    s = input().split()
    for temp in lst:
        if temp.id == s[0]:
            temp.diemDanh(s[1])
for temp in lst:
    print(temp)

"""
3
B19DCCN999
Le Cong Minh
D19CQAT02-B
B19DCCN998
Tran Truong Giang
D19CQAT02-B
B19DCCN997
Nguyen Tuan Anh
D19CQCN04-B
B19DCCN998 xxxmxmmvmx
B19DCCN997 xmxmxxxvxx
B19DCCN999 xvxmxmmvvm
"""