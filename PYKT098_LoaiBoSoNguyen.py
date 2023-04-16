from re import findall

f = open("DATA.in", "r")
lst = []
while True:
    s = f.readline()
    if s == "":
        break
    lst += s.split()
lst = sorted(lst)
for i in lst:
    if not i.isdigit():
        print(i, end=" ")
    else:
        if int(i) < -2147483648 or int(i) > 2147483647:
            print(i, end=" ")