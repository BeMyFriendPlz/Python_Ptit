class ThiSinh:
    def __init__(self, a, b, c, d, e) -> None:
        self.name = a
        self.birth = b
        self.total = c + d + e
    
    def prin(self):
        print(self.name + " " + self.birth + " " + "{:.1f}".format(self.total))

t = ThiSinh(input(), input(), float(input()), float(input()), float(input()))
t.prin()