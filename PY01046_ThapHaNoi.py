def chuyen(n, a, b):
    print(a, '->', b)

def thapHaNoi(n, a, b, c):
    if n == 1: chuyen(1, a, c)
    else:
        thapHaNoi(n - 1, a, c, b)
        chuyen(n, a, c)
        thapHaNoi(n - 1, b, a, c)

n = int(input())
thapHaNoi(n, 'A', 'B', 'C')