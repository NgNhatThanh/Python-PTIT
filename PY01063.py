t = int(input())
for i in range(t):
    s = input()
    n = input()
    cnt = 0
    j = 0
    while j < len(s) - len(n) + 1:
        if s[j: j + len(n)] == n:
            cnt += 1
            j += len(n) - 1
        j += 1
    print(cnt)
