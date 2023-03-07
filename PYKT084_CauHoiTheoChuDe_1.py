n = int(input())
lst = []    
for i in range(n):
    a = input()
    if a == "":
        print(f"{lst[0]}: {len(lst) - 1}")
        lst.clear()
    else: 
        lst.append(a)
print(f"{lst[0]}: {len(lst) - 1}")