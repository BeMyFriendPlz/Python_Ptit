if __name__ == '__main__':
    t = int(input())
    lst = []
    for i in range(t):
        lst.append([x for x in input().split()])
    i = 0
    ans = []
    while i < t:
        if len(lst[i]) == 6:
            i += 2
            ans.append(1)
            while i < t and len(lst[i]) == 6:
                i += 2
        elif len(lst[i]) == 7:
            i += 4
            ans.append(2)
    print(len(ans))
    for i in ans:
        print(i)