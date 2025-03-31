t = int(input())
for _ in range(t):
    n = int(input())
    lst = [list(map(float, input().split())) for i in range(n)]
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        dp[i] = 1
        for j in range(i):
            if lst[i][0] > lst[j][0] and lst[i][1] < lst[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))