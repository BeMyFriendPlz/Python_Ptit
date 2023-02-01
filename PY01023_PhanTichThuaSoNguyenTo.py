import math

t = int(input())
for i in range (t):
    ans = {}
    n = int(input())
    for i in range (2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            if i in ans:
                ans[i] += 1
            else:
                ans[i] = 1
            n /= i
    if n > 1:
        ans[int(n)] = 1
    print("1", end=" ")
    for i in ans:
        print(f"* {i}^{ans[i]}", end=" ")
    print()