import math
from decimal import Decimal

class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b
    
    def distance(self, P):
        ans = math.sqrt((self.x - P.x) ** 2 + (self.y - P.y) ** 2)
        return "{:.4f}".format(ans)

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1