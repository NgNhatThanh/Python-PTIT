n = int(input())
lst = [input().strip() for _ in range(n)]
i = 0
while i < n:
    cd = lst[i]
    i += 1
    cnt = 0
    while i < n and len(lst[i]) > 0:
        cnt += 1
        i += 1
    print(cd + ': ' + str(cnt))
    i += 1