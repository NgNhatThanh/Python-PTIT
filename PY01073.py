s = input()
n = len(s)

a = [0] * n

def Try(str, i):
    if i == n:
        print(str)
        return
    for j in range(n):
        if a[j] == 0:
            a[j] = 1
            Try(str + s[j], i + 1)
            a[j] = 0

Try("", 0)