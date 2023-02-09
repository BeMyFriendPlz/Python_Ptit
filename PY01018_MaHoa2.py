P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

def findCharacter(k, c):
    return P[(k + P.find(c)) % 28]

while True:
    string = input()
    if string == "0": break
    k, s = [x for x in string.split()]
    ans = ""
    for c in s:
        ans = findCharacter(int(k), c) + ans
    print(ans)