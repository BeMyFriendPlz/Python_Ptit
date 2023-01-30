def check(n):
    for c in n:
        if c != "4" and c != "7":
            return False
    return True

t = int(input())
for i in range (t):
    n = input()
    if(check(n)):
        print("YES")
    else:
        print("NO")   