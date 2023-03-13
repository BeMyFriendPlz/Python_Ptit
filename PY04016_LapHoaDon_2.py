import datetime

class KhachHang:
    def __init__(self, id, name, room, start, end, phatSinh) -> None:
        self.id = "KH{:02d}".format(id)
        self.name = name
        self.room = room
        self.phatSinh = phatSinh
        format = "%d/%m/%Y"
        date1 = datetime.datetime.strptime(start, format).date()
        date2 = datetime.datetime.strptime(end, format).date()
        self.soNgay = 1 + (date2 - date1).days
    
    def chiPhiPhong(self):
        if self.room[0] == '1':
            return 25 * self.soNgay
        elif self.room[0] == '2':
            return 34 * self.soNgay
        elif self.room[0] == '3':
            return 50 * self.soNgay
        else:
            return 80 * self.soNgay
    
    def tongTien(self):
        return self.phatSinh + self.chiPhiPhong()

    def __str__(self) -> str:
        return "{} {} {} {} {}".format(self.id, self.name, self.room, self.soNgay, self.tongTien())

if __name__ == "__main__":
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(KhachHang(i+1, input(), input(), input().strip(), input().strip(), int(input())))
    lst.sort(key=lambda x : -x.tongTien())
    for i in lst:
        print(i)
