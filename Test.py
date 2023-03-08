def encode(s):
    ans = ''
    for i in s:
        if i in banMa:
            index = banMa.index(i)
            ans += maHoa[index]
        else:
            ans += i
    return ans

def decode(s):
    ans = ''
    for i in s:
        if i in maHoa:
            index = maHoa.index(i)
            ans += banMa[index]
        else:
            ans += i
    return ans

banMa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

s = input()
for i in range(1, 26):
    maHoa = [chr((ord(x)-ord('A') + i) % 26 + ord('A')) for x in banMa]
    print(f"Giải mã {i}: {decode(s)}")