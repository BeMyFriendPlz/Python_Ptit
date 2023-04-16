N = 10**18
list = []

i = 1
while i <= N:
    j = 1
    while j <= N:
        k = 1
        while k <= N:
            list += [i * j * k]
            k *= 5
        j *= 3
    i *= 2
list.sort()

dic = {}
for i in range(len(list)):
    dic[list[i]] = i + 1

t = int(input())
for i in range(t):
    n = int(input())
    if n in dic: print(dic[n])
    else: print("Not in sequence")