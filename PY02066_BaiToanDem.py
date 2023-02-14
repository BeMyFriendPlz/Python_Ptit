n = int(input())
lst = []
while True:
    lst += [int(x) for x in input().split()]
    if len(lst) == n: break
max = lst[-1]
check = True
for i in range(1, max):
    if i not in lst:
        check = False
        print(i)
if check:
    print("Excellent!")