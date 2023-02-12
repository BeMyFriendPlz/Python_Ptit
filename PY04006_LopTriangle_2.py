import math

class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b
    
    def distance(self, P):
        ans = math.sqrt((self.x - P.x) ** 2 + (self.y - P.y) ** 2)
        return ans

class Triangle:
    def __init__(self, p1, p2, p3):
        self.c1 = p1.distance(p2)
        self.c2 = p2.distance(p3)
        self.c3 = p3.distance(p1)

    def DienTich(self):
        if (self.c1 + self.c2 <= self.c3) or (self.c1 + self.c3 <= self.c2) or (self.c2 + self.c3 <= self.c1):
            print("INVALID")
        else:
            a = self.c1
            b = self.c2
            c = self.c3
            s = math.sqrt((a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c)) / 4
            print("{:.2f}".format(s))
        

t = int(input())
lst = []
for i in range (t):
    lst += [float(x) for x in input().split()]
n = 0
for i in range(t):
    tri = Triangle(Point(lst[n], lst[n+1]), Point(lst[n+2], lst[n+3]), Point(lst[n+4], lst[n+5]))
    tri.DienTich()
    n += 6