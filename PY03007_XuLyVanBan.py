import re
s = ""
while True:
    try:
        s += input()
    except:
        break
s = re.findall("[\w\s:,]+",s)
for i in s:
    temp = i.lower().split()
    temp[0] = temp[0].title()
    print(' '.join(temp))