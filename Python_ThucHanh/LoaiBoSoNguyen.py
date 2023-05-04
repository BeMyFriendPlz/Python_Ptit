f = open("DATA.in", "r")
lst = []
for x in f.read().split("\n"):
    lst += x.split()
f.close()

lst.sort()
for i in lst:
    if not i.isdigit():
        print(i, end=" ")
    else:
        if int(i) < -2147483648 or int(i) > 2147483647:
            print(i, end=" ")
