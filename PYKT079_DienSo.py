t = int(input())
for i in range (t):
    n = int(input())
    lst = list({int(x) for x in input().split()})
    print(lst[-1] - lst[0] + 1 - len(lst))