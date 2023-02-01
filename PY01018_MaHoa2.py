P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

def findCharacter(k, c):
    for i in range (len(P)):
        if c == P[i]:
            return P[(k + i) % 28]

while True:
    string = input()
    if string == "0": break
    k, s = [x for x in string.split()]
    ans = ""
    for c in s:
        ans = findCharacter(int(k), c) + ans
    print(ans)