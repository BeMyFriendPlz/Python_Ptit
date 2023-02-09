class Rectangle:
    def __init__(self, a, b, c):
        self.dai = a
        self.rong = b
        self.mau = c
    
    def perimeter(self):
        return self.dai * 2 + self.rong * 2

    def area(self):
        return self.dai * self.rong
    
    def color(self):
        return self.mau[0].upper() + self.mau[1:].lower()

    def check(self):
        if self.dai <= 0 or self.rong <= 0: return False
        return True

    def output(self):
        if self.check():
            print('{} {} {}'.format(self.perimeter(), self.area(), self.color()))
        else:
            print("INVALID")

arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
r.output()