f = open("CONTACT.in", "r")
lst = f.read().split("\n")
s = sorted(set(x.lower() for x in lst))
print(*s, sep="\n")