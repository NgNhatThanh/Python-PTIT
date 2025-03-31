def check(arr):
    s = ''.join(map(str, arr))
    a, b = s.split(' = ')
    a = str(int(eval(a)))
    if len(a) != 2 or a[0] == '-':
        return False
    if (b[0] != '?' and b[0] != a[0]) or (b[1] != '?' and b[1] != a[1]):
        return False
    return True


def Try(s, i):
    if i == 7:
        if check(s):
            bt = ''.join(map(str, s[:7]))
            s[-2:] = list(str(eval(bt)))
            res = ''.join(map(str, s))
            print(res)
            return True
        return False
    if s[i] != '?':
        return Try(s, i + 1)
    c = []
    if i == 3:
        c = ['+', '-']
    else:
        st = 0
        if i == 0 or i == 5:
            st = 1
        for k in range(st, 10):
            c.append(str(k))
    for k in c:
        s[i] = k
        res = Try(s, i + 1)
        if res:
            return True
        else:
            s[i] = '?'
    return False


t = int(input())
for _ in range(t):
    s = list(input())
    if s[3] == '/' or s[3] == '*':
        print("WRONG PROBLEM!")
    else:
        if not Try(s, 0):
            print("WRONG PROBLEM!")

