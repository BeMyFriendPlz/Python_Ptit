class MonThi:
    def __init__(self, a, b ,c) -> None:
        self.ma = a
        self.mon = b
        self.thi = c

    def __str__(self) -> str:
        return self.ma + " " + self.mon + " " + self.thi
n = int(input())
lst = []
for i in range(n):
    lst.append(MonThi(input(), input(), input()))
lst.sort(key=lambda x:x.ma)
print(*lst, sep="\n")