def check(s):
    lst = s.split('.')
    if len(lst) > 2: return False
    if lst[1] != 'py': return False
    for c in lst[0]:
        if (c < 'a' or c > 'z') and (c != '_'):
            return False
    return True
        
s = input().strip().lower()
if check(s):
    print("yes")
else:
    print("no")