class SoPhuc:
    def __init__(self, a, b):
        self.x = a
        self.y = b
    
    def cong(self, soPhuc):
        a = self.x + soPhuc.x
        b = self.y + soPhuc.y
        return SoPhuc(a, b)
    
    def nhan(self, soPhuc):
        a = self.x * soPhuc.x - self.y * soPhuc.y
        b = self.x * soPhuc.y + self.y * soPhuc.x
        return SoPhuc(a, b)
    
    def __str__(self) -> str:
        if self.y > 0:
            return "{} + {}i".format(self.x, self.y)
        else:
            return "{} - {}i".format(self.x, -self.y)

t = int(input())
for i in range(t):
    lst = [int(x) for x in input().split()]
    a = SoPhuc(lst[0], lst[1])
    b = SoPhuc(lst[2], lst[3])
    c = a.cong(b)
    print(f"{c.nhan(a)}, {c.nhan(c)}")