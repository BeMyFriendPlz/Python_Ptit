t = int(input())
for i in range (t):
    s = [x for x in input().split()]
    length = 0
    for string in s:
        if length + len(string) > 100:
            break
        else:
            print(string, end=" ")
            length += len(string) + 1
    print()