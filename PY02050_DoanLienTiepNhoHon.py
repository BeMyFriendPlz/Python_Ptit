t = int(input())
for i in range (t):
    n = int(input())
    lst = [int(x) for x in input().split()]
    st = []
    for i in range (n):
        while(len(st) > 0 and lst[st[-1]] <= lst[i]): st.pop()
        if len(st) == 0:
            print(i + 1, end=' ')
        else:
            print(i - st[-1], end=' ')
        st.append(i)
    print()