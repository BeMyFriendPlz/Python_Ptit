def coSo10(s):
    sum = 0
    for i in range (len(s)):
        if s[i] == "1":
            sum += 2 ** i
    return sum

def coSoX(n, k):
    ans = ""
    while n > 0:
        num = n % k
        if num > 9:
            ans += chr(ord("A") + (num % 10))
        else:
            ans += str(num)
        n //= k
    return ans[::-1]

t = int(input())
for i in range (t):
    k = int(input())
    s = input()[::-1]
    print(coSoX(coSo10(s), k))