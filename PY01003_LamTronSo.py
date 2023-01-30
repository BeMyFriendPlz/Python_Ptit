t = int(input())
for i in range (t):
    n = input()
    k = len(n) - 1
    nho = 0
    ans = ""
    while k > 0:
        temp = int(n[k])
        if nho == 1:
            temp += 1
            nho = 0
        if temp >= 5:
            nho = 1
        ans = "0" + ans
        k -= 1
    temp = 0
    if(nho == 1):
        temp = int(n[0]) + 1
    else:
        temp = int(n[0])
    print(str(temp) + ans)