n = int(input())
lst = sorted([int(x) for x in input().split()])
op1 = lst[0] * lst[1]
op2 = lst[0] * lst[1] * lst[-1]
op3 = lst[-1] * lst[-2]
op4 = lst[-1] * lst[-2] * lst[-3]
print(max(op1, max(op2, max(op3, op4))))