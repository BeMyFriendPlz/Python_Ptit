def tong(s):
    sum = 0
    for i in s:
        sum += ord(i) - ord('0')
    return sum

s = input()
dem = 0
while len(s) > 1:
    s = str(tong(s))
    dem += 1
print(dem)