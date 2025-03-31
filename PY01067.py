ans = []

for i in range(2, 10001):
    tmp = ''
    cnt = 0
    while i > 0:
        tmp += chr(i % 3 + ord('0'))
        if i % 3 == 2:
            cnt += 1
        i //= 3
    if cnt > len(tmp) // 2:
        tmp = tmp[::-1]
        ans.append(tmp)

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(n):
        print(ans[i], end = ' ')
    print()