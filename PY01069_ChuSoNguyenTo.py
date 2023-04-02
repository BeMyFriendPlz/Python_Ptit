ans = []
def Try(x):
    if len(x) >= 4:
        if '2' in x and '3' in x and '5' in x and '7' in x and x[-1] != '2':
            ans.append(x)
    if len(x) == n:
        return
    Try(x + '2')
    Try(x + '3')
    Try(x + '5')
    Try(x + '7')

n = int(input())
Try('')
ans.sort(key=lambda x : len(x))
print(*ans, sep="\n")


