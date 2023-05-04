mod = 1000
class c:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def __str__(self) -> str:
        return f'{self.x} {self.y}'
def mul(a, b):
    r = c(0, 0)
    r.x = (a.x*b.x + 5*a.y*b.y)%mod
    r.y = (a.x*b.y + a.y*b.x)%mod
    return r
def mu(a, b):
    if b == 0:
        return c(1, 0)
    if b&1:
        return mul(mu(a, b-1), a)
    p = mu(a, b>>1)
    return mul(p, p)
x = c(3, 1)

t = int(input())
cnt = 0

while t > 0:
    t -= 1
    cnt += 1
    print(f'Case #{cnt}:',str(mu(x, int(input())).x*2%mod - 1).zfill(3))

"""
2
5
2
"""