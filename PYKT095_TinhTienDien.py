class KhachHang:
    def __init__(self, id, name, information) -> None:
        self.id = "KH{:02d}".format(id)
        self.name = " ".join([x.lower().title() for x in name.strip().split()])
        temp = information.split()
        self.hoGiaDinh = temp[0]
        self.cSoDau = int(temp[1])
        self.cSoCuoi = int(temp[2])

    def dinhMuc(self):
        return 100 if self.hoGiaDinh == "A" else 500 if self.hoGiaDinh == "B" else 200

    def tienTrongDM(self):
        soDien = self.cSoCuoi - self.cSoDau
        return soDien * 450 if soDien < self.dinhMuc() else self.dinhMuc() * 450
    
    def tienVuotDM(self):
        soDien = self.cSoCuoi - self.cSoDau
        return 0 if soDien < self.dinhMuc() else (soDien - self.dinhMuc()) * 1000
    
    def thueVAT(self):
        return self.tienVuotDM() // 20
    
    def tongTien(self):
        return self.tienTrongDM() + self.tienVuotDM() + self.thueVAT()
    
    def __str__(self) -> str:
        return "{} {} {} {} {} {}".format(self.id, self.ten, self.tienTrongDM(), self.tienVuotDM(), self.thueVAT(), self.tongTien())
    
if __name__ == "__main__":
    t = int(input())
    lst = []
    for i in range(t):
        lst.append(KhachHang(i+1, input(), input()))
    lst.sort(key=lambda x : -x.tongTien())
    print(*lst, sep="\n")