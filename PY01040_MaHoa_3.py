char_to_num = {}
num_to_char = {}
for i in range (0, 26):
    char_to_num[chr(ord("A") + i)] = i
    num_to_char[i] = chr(ord("A") + i)

def devide(s):
    return s[:len(s)//2], s[len(s)//2:]

def rotate(s):
    sum = 0
    for c in s:
        sum += char_to_num[c]
    ans = ""
    for c in s:
        ans += num_to_char[(char_to_num[c] + sum) % 26]
    return ans

def merge(s1, s2):
    ans = ""
    for i in range(len(s1)):
        ans += num_to_char[(char_to_num[s1[i]] + char_to_num[s2[i]]) % 26]
    return ans

t = int(input())
for i in range(t):
    s = input()
    s1, s2 = devide(s)
    print(merge(rotate(s1), rotate(s2)))
    