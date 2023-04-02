class CaThi:
    def __init__(self, a, b, c, d) -> None:
        self.id = "C{:003d}".format(a)
        self.date = b
        self.time = c
        self.room = d
        self.day, self.month, self.year = map(int, b.split("/"))
        self.hour, self.min = map(int, c.split(":"))

    def __str__(self) -> str:
        return "{} {} {} {}".format(self.id, self.date, self.time, self.room)

f = open("CATHI.in", "r")
a = f.read().split()
lst, x = [], 0
for i in range(int(a[0])):
    lst.append(CaThi(i + 1, a[x+1], a[x+2], a[x+3]))
    x += 3
lst.sort(key=lambda x : (x.year, x.month, x.day, x.hour, x.min))
print(*lst, sep="\n")

"""
2
09/01/2022
15:30
70172
09/01/2022
10:00
70279
"""