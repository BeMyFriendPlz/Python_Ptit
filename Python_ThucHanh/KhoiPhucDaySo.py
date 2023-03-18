n = int(input())
lst = []
for i in range(n):
    lst.append([int(x) for x in input().split()])
if n == 2:
    print("1 1")
else:
    a = (lst[0][1] + lst[0][2] - lst[1][2]) // 2
    print(a, end=" ")
    for i in range(1, n):
        print(lst[0][i] - a, end=" ")
    print()

"""
2
0 2
2 0
"""
"""
4
0 3 6 7
3 0 5 6
6 5 0 9
7 6 9 0
"""