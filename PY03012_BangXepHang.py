import functools

class SinhVien:
    def __init__(self, name, correct, submit):
        self.name = name
        self.correct = correct
        self.submit = submit

def cmd(a, b):
    if a.correct == b.correct:
        if a.submit == b.submit:
            return 1 if a.name > b.name else -1
        else:
            return 1 if a.submit > b.submit else -1
    else:
        return 1 if a.correct < b.correct else -1

n = int(input())
sv = []
for i in range(n):
    s = input()
    a, b = [int(x) for x in input().split()]
    sv.append(SinhVien(s, a, b))
sv = sorted(sv, key = functools.cmp_to_key(cmd))
for i in sv:
    print(i.name, i.correct, i.submit)