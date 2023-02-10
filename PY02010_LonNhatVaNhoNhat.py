while True:
    n = int(input())
    if n == 0: break
    lst = []
    for i in range(n):
        lst.append(int(input()))
    lst.sort()
    if lst[0] == lst[-1]:
        print("BANG NHAU")
    else:
        print(lst[0], lst[-1])