def doiDiem(s):
    if s >= 39:
        return 9.0
    elif s >= 37:
        return 8.5
    elif s >= 35:
        return 8.0
    elif s >= 33:
        return 7.5
    elif s >= 30:
        return 7.0
    elif s >= 27:
        return 6.5
    elif s >= 23:
        return 6.0
    elif s >= 20:
        return 5.5
    elif s >= 16:
        return 5.0
    elif s >= 13:
        return 4.5
    elif s >= 10:
        return 4.0
    elif s >= 7:
        return 3.5
    elif s >= 5:
        return 3.0
    elif s >= 3:
        return 2.5

t = int(input())
for i in range(t):
    s = [float(x) for x in input().split()]
    sum = (doiDiem(int(s[0])) + doiDiem(int(s[1])) + s[2] + s[3]) / 4
    if sum - int(sum) >= 0.75:
        print(int(sum) + 1.0)
    elif sum - int(sum) >= 0.25:
        print(int(sum) + 0.5)
    else:
        print(int(sum))