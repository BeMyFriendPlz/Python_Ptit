def transfer(s):
    dic = {}
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic

def check(dic1, dic2):
    for i in dic2:
        if i not in dic1:
            return False
        else:
            if dic2[i] != dic1[i]:
                return False
    return True

t = int(input())
for i in range (t):
    s1 = input()
    s2 = input()
    print(f"Test {i+1}:", end=' ')
    if len(s1) != len(s2):
        print("NO")
        continue
    dic1 = transfer(s1)
    dic2 = transfer(s2)
    if check(dic1, dic2):
        print("YES")
    else:
        print("NO")