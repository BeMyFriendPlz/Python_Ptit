n = int(input())
lst = [int(x) for x in input().split()]
k = 0
while k < (len(lst) -1):
    if (lst[k] +  lst[k+1]) % 2 == 0:
        lst.pop(k)
        lst.pop(k)
        k -= 2
    k += 1
    if k < 0: k = 0
print(len(lst))