t = int(input())
for i in range(t):
    n = int(input())
    x, y, z = [int(x) for x in input().split()]
    Queue, ans = [], [-1] * 111
    ans[0] = 0
    Queue.append((0, 0))
    while len(Queue) > 0:
        a, b = Queue[-1]
        Queue.pop()
        if a+1 < 110 and (ans[a+1] == -1 or ans[a+1] > b+x):
            ans[a+1] = ans[a] + x
            Queue.append((a+1, b+x))
        if a-1 > 0 and (ans[a-1] == -1 or ans[a-1] > b+y):
            ans[a-1] = ans[a] + y
            Queue.append((a-1, b+y))
        if a*2 < 110 and (ans[a*2] == -1 or ans[a*2] > b+z):
            ans[a*2] = ans[a] + z
            Queue.append((a*2, b+z))
    print(ans[n])